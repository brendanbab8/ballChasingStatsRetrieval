import getpass as gp
import subprocess as sp
import json
import xlsxwriter as xlsx
import classes
import spreadsheet as ss
from typing import List

STEAMID = "76561199061858917"
players: List[classes.PlayerData] = []
debug_d = False
debug_ss = True

'''
Communicates with ballchasing.com to retrieve the group stats.
Returns a list of group stats.
'''


def retrieve_stats():
    token = gp.getpass("Enter your authorization token: ")

    print("\n",
          "Executing request: \"https://ballchasing.com/api/groups?creator=" +
          STEAMID + "\"")
    response = sp.check_output("curl -s -H \"Authorization: " + token +
                               "\" \"https://ballchasing.com/api/groups?creator="
                               + STEAMID + "\"", text=True)
    res_obj = json.loads(response)["list"]

    if debug_d:
        print("\n", json.dumps(res_obj, indent=4))

    groups = []

    for group in res_obj:
        groups.append(group["id"])

    if debug_d:
        print("\n", groups)

    stats = []

    for id in groups:
        print("\n", "Executing request: \"https://ballchasing.com/api/groups/" +
              id + "\"")
        response = sp.check_output("curl -s -H Authorization:" + token +
                                   " \"https://ballchasing.com/api/groups/" +
                                   id + "\"", text=True)
        stats.append(json.loads(response))

    return stats


def create_spreadsheet(stats):
    workbook = xlsx.Workbook("stats.xlsx")
    for group in stats:
        name = group["name"]
        team = input(
            f"For group: {name}, what team would you like to extract?")

        for player in group["players"]:

            if player["team"].lower() == team.lower():

                try:  # new player encountered

                    worksheet = workbook.add_worksheet(name=player["name"])
                    player_obj = classes.PlayerData(player["name"], worksheet)
                    player_obj.set_teams(
                        name, player["team"], player["cumulative"])
                    # stats are total, not averages.
                    players.append(player_obj)

                except:  # player already exists.
                    for p in players:
                        if p.get_name() == player["name"]:
                            p.set_teams(
                                name, player["team"], player["cumulative"])

                if debug_ss:
                    print(player["name"])

    if debug_ss:
        for p in players:
            print(p.get_name(), "\n", json.dumps(p.get_teams(), indent=4))

    for p in players:
        ss.create_columns(workbook, p.get_worksheet())
        for row in p.get_teams():
            row_index = p.get_row()
            ss.create_row(p.get_worksheet(), row, row_index)
            p.set_row(row_index + 1)

    workbook.close()


'''
Script execution
'''
stats = retrieve_stats()

if debug_d:
    print("\n", json.dumps(stats, indent=4))

create_spreadsheet(stats)

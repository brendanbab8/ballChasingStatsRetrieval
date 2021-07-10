import getpass as gp
import subprocess as sp
import json

STEAMID = "76561199061858917"
debug = True
'''
Communicates with ballchasing.com to retrieve the group stats.
Returns a list of group stats.
'''
def retrieve_stats():
  token = gp.getpass("Enter your authorization token: ")

  print("\n", 
    "Executing request: \"https://ballchasing.com/api/groups?SteamID64=" + 
    STEAMID + "\"")
  response = sp.check_output("curl -s -H Authorization:" + token + 
    " \"https://ballchasing.com/api/groups?creator=" + STEAMID + "\"", 
    text=True)
  res_obj = json.loads(response)["list"]

  if debug:
    print("\n", json.dumps(res_obj, indent=4))

  groups = []

  for group in res_obj:
    groups.append(group["id"])

  if debug:
    print("\n", groups) 

  stats = []

  for id in groups:
    print("\n", "Executing request: \"https://ballchasing.com/api/groups/" + 
      id + "\"")
    response = sp.check_output("curl -s -H Authorization:" + token + 
      " \"https://ballchasing.com/api/groups/" + id + "\"", text=True)
    stats.append(json.loads(response))
  
  return stats
'''
Script execution
'''
stats = retrieve_stats()

if debug:
  print("\n", json.dumps(stats, indent=4))

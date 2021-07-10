import getpass as gp
import subprocess as sp
import json

STEAMID = "76561199061858917"

token = gp.getpass("Enter your authorization token: ")

response = sp.check_output("curl -s -H Authorization:" + token + " \"https://ballchasing.com/api/groups?creator=" + STEAMID + "\"", text=True)
print("\n", "Executing request: \"https://ballchasing.com/api/groups?SteamID64=" + STEAMID + "\"")
print("\n", json.dumps(json.loads(response), indent=4))
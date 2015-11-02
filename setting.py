
import json
settingfile = open("setting.json", "r")
setting = json.loads(settingfile.read())
settingfile.close()
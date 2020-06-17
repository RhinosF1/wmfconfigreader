import json
import os
os.system('cd mediawiki-config && git pull && composer update && composer buildDBLists && composer buildConfigCache')
wiki = input("Wiki name: ")
file = open('mediawiki-config/wmf-config/config-cache/conf-' + wiki + '.json')
contents = file.read()
contents = json.loads(contents)
func = input("Function (read/check): ")
if func == "read":
    print("Found " + str(len(contents.keys())) + " keys")
    go = contents["groupOverrides"]
    go.update(contents["groupOverrides2"])
    for key in go.keys():
        print(str(key) + " : " + str(go[key]))
    for key in contents.keys():
        if key != "groupOverrides" or key != "groupOverrides2":
            print(str(key) + " : " + str(contents[key]))
if func == "check":
    which = input("Setting/Group/Right: ")
    if which == "Group":
        truelist = []
        falselist = []
        right = input("Group Name: ")
        go = contents["groupOverrides"]
        go.update(contents["groupOverrides2"])
        yes = go.keys()
        if right in yes:
            rightlist = go[right]
            for key in rightlist:
                if rightlist[key]:
                    truelist.append(key)
                if not rightlist[key]:
                    falselist.append(key)
        print("Enabled: ")
        for x in truelist:
            print(x)
        print("Disabled: ")
        for x in falselist:
            print(x)
    if which == "Setting":
        setting = input("Setting: ")
        if setting in contents.keys():
            try:
                for key in contents[setting]:
                    print(key + " : " + str(contents[setting][key]))
            except TypeError:
                print(contents[setting])
    if which == "Right":
        right = input("Right: ")
        go = contents["groupOverrides"]
        go2 = contents["groupOverrides2"]
        go.update(go2)
        grouplist = []
        for key in go.keys():
            group = key
            rightlist = go[key]
            for rkey in rightlist.keys():
                if rkey == right:
                    if rightlist[rkey]:
                        grouplist.append(group)
        print("The following groups have it: ")
        for x in grouplist:
            print(x)

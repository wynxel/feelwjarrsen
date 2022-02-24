from collections import defaultdict

contribs, projects = {"Anna": {"C++": 2}}, {"WebServer": {"DAY": 7, "SCR": 10, "BBF":7, "ROLE": {"HTML": 3, "C++": 2}}}
output = []

# reverse the dictionary
linkedin = {}
for key, value in contribs.items():
    for key2, value2 in value.items():
        if key2 not in linkedin:
            linkedin[key2] = {key: value2}
        else:
            linkedin[key2][key] = value2


for project in projects:
    possible = {role: [] for role in project.keys()}
    is_possible = True
    for role, role_level in project["ROLE"].items():
        if role in linkedin:
            for name, level in linkedin[role].items():
                if level >= role_level:
                    possible[role].append(name)
        if len(possible[role]) == 0:
            is_possible = False
            break
    if not is_possible:
        continue
    possible_tmp = {k: len(v) for k, v in possible.items()}
    possible_lens = {k: v for k, v in sorted(possible_tmp.items(), key=lambda item: item[1])}
    result = set()
    skip = False
    for skill, num in possible_lens.items():
        if num == 1:
            if possible[skill][0] in result:
                skip = True
                break
            result.add(possible[skill][0])
        else:

    if skip:
        continue
    possible = odstran(possible, "Meno cloveka") #
    possible = utried(possible) # kluce (role) su utriedene vzostupne podla poctu ludi ktori ich vedia
    kontroluj(possible) # T: zoznamy su nenulovej dlzky, F: inac



    # ma possible vsetky role vyplnene?
    # ci nie je jeden na dve role ktore nevie nik iny?
    # ak je vsetko ok, pridaj do vysledku

    # pridat do output



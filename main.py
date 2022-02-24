from collections import defaultdict
import input

#contribs, projects = {"Anna": {"C++": 2}}, {"WebServer": {"DAY": 7, "SCR": 10, "BBF":7, "ROLE": {"HTML": 3, "C++": 2}}}
contribs, projects = input.load(), {}
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
    possible = defaultdict(lambda: [])
    for role, role_level in project["ROLE"].items():
        if role in linkedin:
            for name, level in linkedin[role].items():
                if level >= role_level:
                    # {"C++": ["meno1", ...]}
                    possible[role].append(name)
    # ma possible vsetky role vyplnene?
    # ci nie je jeden na dve role ktore nevie nik iny?
    # ak je vsetko ok, pridaj do vysledku

    # pridat do output



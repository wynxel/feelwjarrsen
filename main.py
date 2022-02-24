from collections import defaultdict
from kan import utried, kontroluj, odstran

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


def get_one_full_project():
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
        people = set()

        broken = False
        while possible.__len__() != 0:
            possible = utried(possible)
            if not kontroluj():
                broken = True
                break
            first = list(possible.items())[0]
            first_person = first[1][0]
            first_role = first[0]
            possible = odstran(possible, first_person, first_role)
            people.add(first_person)
        if not broken:
            return project, people
    return False


    # ma possible vsetky role vyplnene?
    # ci nie je jeden na dve role ktore nevie nik iny?
    # ak je vsetko ok, pridaj do vysledku

    # pridat do output



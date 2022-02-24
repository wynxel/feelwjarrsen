def odstran(possible, name, skill):
    del possible[skill]
    for elem in possible:
        if name in possible[elem]:
            possible[elem].remove(name)


def utried(possible):
    lens = {k: len(v) for k, v in possible.items()}
    return {k: possible[k] for k, _ in sorted(lens.items(), key=lambda item: item[1])}


def kontroluj(possible):
    return len(possible) > 0 and len(list(possible.values())[0]) > 0


a = utried({"A": [3,2,1], "B":[2], "C":[2], "X": [3,4,5,6], "w":[]})
kontroluj(a) # flase
del a['w']
kontroluj(a) # true
kontroluj({}) # flase


def print_result(project, contribs: set):
    print(project)
    print(" ".join(contribs))

print_result("meno projektu", set(["Anna", "Joe"]))
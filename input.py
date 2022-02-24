with open("a_an_example.in.txt",'r',encoding = 'ascii|') as f:
    zebydobrebolo = f.read().split('\n')
    first_line = zebydobrebolo[0].split(' ')
    competitors_count = int(first_line[0])
    projects_count = int(first_line[1])
    zebydobrebolo = zebydobrebolo[1:]

x = dict()
skills = 0
for i in range(competitors_count):
    curr_contributor_skills = zebydobrebolo[i + skills].split(' ')
    curr_contributor = curr_contributor_skills[0]
    curr_skill_counts = int(curr_contributor_skills[1])
    print(curr_skill_counts)
    all_skills = dict()
    skills += curr_skill_counts
    for j in range(curr_skill_counts):
        skill = zebydobrebolo[i + skills + j].split(' ')
        all_skills[skill[0]] = int(skill[1])
    x[curr_contributor] = all_skills



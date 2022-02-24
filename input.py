with open("input/a_an_example.in.txt",'r',encoding = 'ascii|') as f:
    zebydobrebolo = f.read().split('\n')
    first_line = zebydobrebolo[0].split(' ')
    competitors_count = int(first_line[0])
    projects_count = int(first_line[1])
    zebydobrebolo = zebydobrebolo[1:]

x = dict()
skills = 0
for i in range(competitors_count):
    curr_contributor_skills = zebydobrebolo[skills].split(' ')
    curr_contributor = curr_contributor_skills[0]
    curr_skill_counts = int(curr_contributor_skills[1])
    all_skills = dict()
    for j in range(curr_skill_counts):
        skill = zebydobrebolo[skills + j + 1].split(' ')
        all_skills[skill[0]] = int(skill[1])
    skills += curr_skill_counts + 1
    x[curr_contributor] = all_skills
print(zebydobrebolo[skills:])
{"WebServer": {"DAY": 7, "SCR": 10, "BBF": 7, "ROLE": {"HTML": 3, "C++": 2}}}
print(x)

def sort_projects(projects):

    project_score = {proj: 0 for proj in projects.keys()}

    for project in projects.keys():
        project_score[project] = (projects["SCR"] + projects["BBF"]) / (projects["DAY"] * (sum(projects["ROLE"][skill] for skill in projects["ROLE"])))

    return sorted(project_score.items(), key=lambda x: x[1], reverse=True)
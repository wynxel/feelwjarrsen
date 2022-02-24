def get_contributors_project():
    zebydobrebolo = load()
    first_line = zebydobrebolo[0].split(' ')
    competitors_count = int(first_line[0])
    projects_count = int(first_line[1])
    zebydobrebolo = zebydobrebolo[1:]
    contributors = dict()
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
        contributors[curr_contributor] = all_skills
    zebydobrebolo = zebydobrebolo[skills:]

    line = 0
    projects = dict()
    for i in range(projects_count):
        curr_project = zebydobrebolo[line].split(' ')
        project_name, day, score, bbf, roles = \
            curr_project[0], int(curr_project[1]), int(curr_project[2]), int(curr_project[3]), int(curr_project[4])
        all_roles = dict()
        for j in range(roles):
            role = zebydobrebolo[line + j + 1].split(' ')
            all_roles[role[0]] = int(role[1])
        line += roles + 1
        projects[project_name] = {"DAY": day, "SCR": score, "BBF": bbf, "ROLE": all_roles}
    return contributors, projects


def load():
    with open("input/a_an_example.in.txt",'r',encoding = 'ascii|') as f:
        zebydobrebolo = f.read().split('\n')
    return zebydobrebolo


def sort_projects(projects):
    project_score = {proj: 0 for proj in projects.keys()}

    for project in projects.keys():
        project_score[project] = (projects["SCR"] + projects["BBF"]) / (projects["DAY"] * (sum(projects["ROLE"][skill] for skill in projects["ROLE"])))

    return sorted(project_score.items(), key=lambda x: x[1], reverse=True)
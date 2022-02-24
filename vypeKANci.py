
class MapCSP():
    def __init__(self, projects, neighbours):
        # List of available contributorself.contributor
        self.contributor_options = ['red', 'green', 'blue', 'yellow']
        self.projects = projects
        self.neighbours = neighbours  # CODE HERE
        self.contributor = {s: None for s in self.projects}

    def print_(self):
        # Prints all projects and their contributorself.contributor
        for s in sorted(self.projects):
            print('{} has contributor: {}'.format(s, self.get_contributor(s)))
        print()


    def set_contributor(self, project, contributor):
        # Assign contributor to a project
        self.contributor[project] = contributor

    def del_contributor(self, project):
        # Remove contributor from project - reset to None
        self.contributor[project] = None

    def get_contributor(self, project):
        # Get contributor assigned to a project
        return self.contributor[project]

    def has_contributor(self, project):
        # Returns True if project has already a contributor
        return self.contributor[project] != None

    def same_contributors(self, project1, project2):
        # Returns True if project1 and project2 are contributored with the same contributor.
        return self.has_contributor(project1)  and  self.get_contributor(project1) == self.get_contributor(project2)

    def all_contributored(self):
        # Returns True if all projects of the map are already contributored.
        return all([self.has_contributor(s) for s in self.projects])

    def is_correct_contributoring(self):
        # Returns True if contributoring is all correct, False if not. Prints the result with found error (if any).
        print('contributoring is ', end='')
        for s1 in self.projects:
            if self.get_contributor(s1) not in self.contributor_options:
                print('INCORRECT - {} has invalid contributor: {}\n'.format(s1, self.get_contributor(s1)))
                return False
            for s2 in self.neighbours[s1]:
                if self.same_contributors(s1,s2):
                    print('INCORRECT - {} and {} have conflicting contributor {}\n'.format(s1, s2, mapa.get_contributor(s1)))
                    return False
        print('OK\n')
        return True


    def can_set_contributor(self, project, contributor):
        # Returns True if we can set contributor to a project without violating constrains - all neighbouring
        # projects must have None or different contributor.
        for i in self.neighbours[project]:
             if contributor == self.get_contributor(i):
                return False
        return True

    def select_next_state(self):
        # Selects next project that will be contributored, or returns False if no such exists (all stated are
        # contributored). You can use heuristics or simply choose a project without contributor for start.
        def project_contrib(susedia):
            return set(self.get_contributor(project) for project in susedia if self.has_contributor(project))
        # zisti mi od susedov ake maju farby,
        # aby som ich potom mohol odcitat od vsetkych farieb a vybrat taky stat, ktory bude mat co najmenej moznosti, cize ma okolo seba zafarbene vela
        
        unsigned_contributors = []                  # klasicka heuristika MRV, opisana je vyssie
        for project in self.projects:
            if not self.has_contributor(project):   
                unsigned_contributors.append(project)

        # odcitam dlzku jednotlivych susedov od dlzky vsetkych, aby som dostal na prve miesto ten stat, ktory ma co najmenej moznosti
        all_contributors = set(self.contributor_options)
        unsigned_contributors.sort(key=lambda x: len(all_contributors - set(project_contrib(self.neighbours[x]))), reverse = True)

        if len(unsigned_contributors) > 0:
            return unsigned_contributors.pop()
        return False


    def contributor_map(self):
        # Assign contributorself.contributor to all projects on the map. (! Beware: 'map' is python`s reserved word - function)
        if self.all_contributored():
            return True
        x = self.select_next_state()
        for contributor in self.contributor_options:
            if self.can_set_contributor(x, contributor):

                self.set_contributor(x, contributor)

                if self.contributor_map():
                    return True

                self.del_contributor(x)
 
        return False
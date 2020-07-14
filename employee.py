class Employee():
    staff = []

    def __init__(self, name):
        self.name = name
        self.skills = []
        self.add_staff()
        self.salary = ''
        self.title = ''

    def add_staff(self):
        self.staff.append(self.name)
        print('{} was added to staff list'.format(self.name))

    def see_staff(self):
        print('Staff list: ')
        for person in self.staff:
            print(person)

    def add_skills(self, skill):
        self.skills.append(skill)

    def see_skills(self):
        print('skills of {} : '. format(self.name))
        for skill in self.skills:
            print(skill)
            
    def add_salary(self, salary):
        self.salary.append(salary)

    def add_title(self, title):
        self.title.append(title)

    def see_attribute(self):
        print('attributes of {} : skills: {} \n title: {} \n salary: {}'
              .format(self.name, self.skills, self.title, self.salary))

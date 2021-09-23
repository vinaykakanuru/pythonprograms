class Student:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def write(self):
        print(f'{self.name} can able to write')

    def read(self):
        print(f'{self.name} can able to read')


class School(Student):
    def __init__(self, id, name, place, course):
        super().__init__(id, name)
        self.place = place
        self.course = course

    def plan(self):
        print(f'Student - {self.name} enrolled to {self.course}')


student = Student('1', 'Vinay')
student.read()

school = School('1', 'Vinay', 'Bangalore', 'AI/ML')
school.plan()


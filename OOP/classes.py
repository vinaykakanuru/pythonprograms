# Base class with public member functions with a constructor
class Student:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def write(self):
        print(f'{self.name} can able to write')

    def read(self):
        print(f'{self.name} can able to read')


# Derived class with public member functions with a Super class constructor
class School(Student):
    def __init__(self, id, name, place, course):
        super().__init__(id, name)
        self.place = place
        self.course = course

    def plan(self):
        print(f'Student - {self.name} enrolled to {self.course}')


# creating object for Base class 
student = Student('1', 'Vinay')
student.read()


# creating Derived class using Base class constructor alongside adding few more arguments
school = School('1', 'Vinay', 'Bangalore', 'AI/ML')
school.plan()

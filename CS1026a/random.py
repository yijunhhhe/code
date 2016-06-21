class Person:
    def __init__(self, name, yearBirth):
        self._name = name
        self._yearBirth = yearBirth
        self._nationality = ""

    def setNationality(self, nationality):
        self._nationality = nationality

    def getName(self):
        return self._getName

    def __repr__(self):
        return self._name + " is" + str((2016 - self._yearBirth) +" years old"

class Instructor(Person):
    def __init__(self, name, yearBirth, salary, faculty):
        super().__init__(name, yearBirth)
        self._salary = salary
        self._faculty = faculty
        self._course = []

    def addCourses(self, ):

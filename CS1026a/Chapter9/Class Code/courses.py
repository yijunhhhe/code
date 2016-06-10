class Courses:
    MAXNUM = 100
    def __init__(self, n):
        self._name = n
        self._dos = dict()

    def addStudent(self, fullName, studentN):
        if len(self._dos) < Courses.MAXNUM:
            self._dos[studentN] = [fullName, 100]
        else:
            print('Sorry the class is full and there is no waitlist :( ')

    def updateStudentScore(self, studentN, newScore):
        if studentN in self._dos:
            self._dos[studentN][1] = newScore
        else:
            print('The student does not exist')

    def printAllStdentsByScore(self):
        for students in self._dos.values():
            print(students[1])

        for key in self._dos:
            print(self._dos[key][1])


        for (key, value) in self._dos.items():
            print(value[1])


    def findAverage(self):
        total = 0
        for student in self._dos:
            total = total + self._dos[student][1]

        return total/len(self._dos)
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

student1 = Student("Yijun",50)
student1.age = 8

print(student1.age)
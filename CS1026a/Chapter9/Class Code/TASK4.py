from student import Student

st1 = Student('Paul', 'Peters')
print('Expecting: Paul Peters')
print(st1.getName())
print('Expecting: 250650111')
print(st1.getStudentNumber())

st1.addCourse('CS1026')
st1.addCourse('MA4312')
st1.addCourse('T')
st1.addCourse('ee')
st1.addCourse('eee')
st1.addCourse('eeeee')
st1.printStudent()

st2 = Student()
st2.printStudent()


class Student :
   _lastStudentNumber = 250650110   #class variable
   MAXCOURSES = 5    #class variable that is constant
   def __init__(self, fName="Kemi", lName="Ola") :
      self._firstName = fName
      self._lastName = lName
      self._fullName = fName + " " + lName
      self._listOfCourses = []
      Student._lastStudentNumber = Student._lastStudentNumber + 1
      self._studentNumber =  Student._lastStudentNumber   #250650111

   def getName(self) :
      return self._fullName

   def getStudentNumber(self):
      return self._studentNumber

   def addCourse(self,cName) :
      if(len(self._listOfCourses) < Student.MAXCOURSES) :
         self._listOfCourses.append(cName)
      else:
         print('You cannot have that many courses')

   def printStudent(self):
      print('Name: ', self._fullName)
      print('Student #: ', self._studentNumber)
      if(len(self._listOfCourses) > 0):
         print('The student is enrolled in the following courses: ')
         for c in self._listOfCourses:
            print(c, end= ', ')
         print()
      else:
         print('The student is not enrolled in any courses')

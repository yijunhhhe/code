numberOfGrades = int(input("Please enter the numebr of grades you want to add: "))

count = 0
total = 0

while count < numberOfGrades:
    grades = float(input("Please enter the grade: "))
    total = total + grades
    count = count + 1
print("the average is",total/count)


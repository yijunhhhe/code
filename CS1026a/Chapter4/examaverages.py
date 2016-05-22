# Obtain the number of exam grades per student
numExams = int(input("How many exam grades does each student have? "))

# Initialize moreGrades to a non-sentinel value
moreGrades = "Y"

# Compute average exam grades until the user wants to stop
while moreGrades == "Y":

    # Compute the average grade for each student
    print("Enter the exam grades.")
    total = 0
    for i in range(1, numExams + 1):
        score = int(input("Exam {}: ".format(numExams)))
        total = total + score

    average = total/numExams
    print("The average is %.2f" % average)

    # Prompt as to whether the user wants to enter grades for another student.
    moreGrades = input("Y/N?")
    moreGrades = moreGrades.upper()

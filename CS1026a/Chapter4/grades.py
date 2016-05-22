# Initialize the counter variables
numPassing = 0
numFailing = 0

# Initialize the variables used to compute the average.
total = 0
count = 0

# Initialize the min and max variables
minGrade = 100.0
maxGrade = 0.0

# Use a while loop with a priming read to ovtain the grades.
grade = float(input("Enter a grade or -1 to finish: "))
while grade >= 0.0:
    # Increment the passing or failing counter
    if grade >= 60.0:
        numPassing = numPassing + 1
    else:
        numFailing = numFailing + 1

    # Determine if the grade is the min or max grade
    if grade > maxGrade:
        maxGrade = grade
    if grade < minGrade:
        minGrade = grade

    # Add the grade to the running total
    total = total + grade
    count = count + 1

    # Read the next grade.
    grade = float(input("Enter a grade or -1 to finish: "))

# Print the results.
if count > 0:
    average = total / count
    print("The average grade is %.2f" % average)
    print(numPassing, numFailing, maxGrade, minGrade)

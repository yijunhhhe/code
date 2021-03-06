# Import math
import math

# Define constants
ADDITIONAL_FEE = 10
CHARGE_OVER_LIMIT_EACH_KM = 0.3
CHARGE_EACH_KILOMETER = 0.3
DAILY_LIMIT_KM = 100
WEEKLY_LIMIT_KM = 2000
age = int()

# Obtain the data from customers
name = input("Please enter your name ")
age = int(input("Please enter your age "))
classificationCode = input("Please enter your classification code ").upper()
numberOfDays = int(input("Please enter the days the vehicle was rented "))
startOdometer = int(input("Please enter odometer reading at the start of the rental period "))
endOdometer = int(input("Please enter odometer reading at the end of the rental period "))
distance = endOdometer - startOdometer
numberOfWeeks = math.ceil(numberOfDays / 7)

# Decide if additional fee would be applied
if age >= 25:
    ADDITIONAL_FEE = 0

# Based on the classification code users choose, compute the total charge
if classificationCode == "B" or classificationCode == "D" or classificationCode == "W":

    # If customers choose the Budget plan
    if classificationCode == "B":
        baseCharge = 20
        totalCharge = baseCharge * numberOfDays + CHARGE_EACH_KILOMETER * distance + ADDITIONAL_FEE * numberOfDays

    # If customers choose the daily plan
    elif classificationCode == "D":
        baseCharge = 50
        if distance <= 100 * numberOfDays:
            totalCharge = baseCharge * numberOfDays + ADDITIONAL_FEE * numberOfDays
        else:
            chargeOverLimit = CHARGE_OVER_LIMIT_EACH_KM * (distance - DAILY_LIMIT_KM * numberOfDays)
            totalCharge = baseCharge * numberOfDays + chargeOverLimit + ADDITIONAL_FEE * numberOfDays

    # If customers choose the weekly plan
    elif classificationCode == "W":
        baseCharge = 200
        if distance <= 1000 * numberOfWeeks:
            totalCharge = baseCharge * numberOfWeeks + ADDITIONAL_FEE * numberOfDays
        elif distance > 1000 * numberOfWeeks and distance <= 2000 * numberOfWeeks:
            totalCharge = (baseCharge + 50) * numberOfWeeks + ADDITIONAL_FEE * numberOfDays
        else:
            chargeOverLimit = CHARGE_OVER_LIMIT_EACH_KM * (distance - WEEKLY_LIMIT_KM * numberOfWeeks)
            totalCharge = (baseCharge + 100) * numberOfWeeks + chargeOverLimit + ADDITIONAL_FEE * numberOfDays

    # Print the result
    print("\nThe customer's name: {}\n"
          "The customer's age: {}\n"
          "The customer's classification code: {}\n"
          "The number of days the vehicle was rented: {}\n"
          "The vehicle's odometer reading at the start of the rental period: {}\n"
          "The vehicle's odometer reading at the end of the rental period: {}\n"
          "The number of kilometers driven during the rental period: {}\n"
          "The amount of money billed to the customer for the rental period ${:.2f}\n"
          .format(name, age, classificationCode, numberOfDays, startOdometer, endOdometer, distance, totalCharge))

# If Users do not enter the correct classification code
else:
    print("\n{} who is {} years old enter the wrong classification code {}.".format(name, age, classificationCode))

# Obtain the input from the users
distance = float(input("Please enter the distance from home to campus: "))
parkingCost = float(input("Please enter the parking cost for each day: "))
fuelEfficiency = float(input("Please enter the fuel efficiency: "))
pricePerLitre = float(input("Please enter the gas price "))
maintenanceCost = float(input("Please enter the maintenance cost for each day: "))
busTicket = float(input("Please enter the bus ticket price: "))
costOfTaxi = float(input("Please enter the cost of Taxt per day: "))

# Define Constants
DAYS_OF_SCHOOL = 50

# Compute the cost of driving car
gasCost = distance * 2 * pricePerLitre / fuelEfficiency
totalCostOfMaintenance = maintenanceCost * distance * 2
semesterCar = (gasCost + parkingCost + totalCostOfMaintenance) * DAYS_OF_SCHOOL

# Compute the cost of taking bus
busWeekdays = 40 * busTicket * 2
sundayTaxiCost = costOfTaxi * 2 * 10
semesterBus = sundayTaxiCost + busWeekdays

if semesterBus < semesterCar:
    print("Take the bus")
else:
    print("Drive your car")

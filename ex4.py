#variables. 

# let's name the variables

cars = 100
space_in_a_car = 4.0
drivers = 30
passsengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passsengers / cars_driven #the error in study drill states that the carpool_capacity was not defined earlier hence we have edited it 


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passsengers, "to carpool today")
print("we need to put about", average_passengers_per_car, "in each car.")

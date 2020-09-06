people = 20
cats = 30 
dogs = 15

if people < cats:
    print("Too many cats! The world id doomed!")

if people > cats:
    print("Not many cats! the world is saved!")

if people < dogs:
    print("The world is drooled on")

if people > dogs:
    print("the world is dry")

dogs += 5 

if people >= dogs:
    print("People are greater than or equal to dogs")

if people <= dogs:
    print("People are less than or equal to dogs")

if people == dogs:
    print("People are dogs!")

people = 40

cars = 30

trucks = 35


if cars > people:
    print("we should take cars.")
elif cars < people:
    print("we should not take cars/")
else:
    print("we can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("May be we could take trucks")
else:
    print("We still can't decide")

if people > trucks:
    print("alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
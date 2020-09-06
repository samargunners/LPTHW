print(""" you enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("what do you do")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input('> ')

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("the bear eats your legs off. good job!")
    else: 
        print(f"well doing {bear} is probably better.")
        print("bear runs away.")

elif door == "2":
    print("you stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespin.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">  ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello")
        print("Good job!")
    else: 
        print("the insanity rots your eyes into a pool of muck")
        print("Good job")

else:
    print("you stumble around and fall on a knife. good job.")
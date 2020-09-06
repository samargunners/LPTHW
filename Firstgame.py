# which bike is for you.

def start():
    print("You need to decide which bike is perfect for you.")
    print("No problem, we will help you select")

    choice = int(input("How old are you?: "))

    if choice in range (18, 36):
        excitingage()
    elif choice in range (36, 51):
        seniorrider()
    elif choice in range (51, 99):
        tooold()
    else:
        underage()

def excitingage():
    print("You seem to be a yound rider")
    print('You have three options to select from Naked Bikes, Sports Bike and Caferacer')
    
    choice = input('What do you select:')

    if choice == "Naked Bike":
        nakedbikes()
    elif choice == "Sports Bike":
        sportsbike()
    else:
        caferacer()

def seniorrider():
    print("you seem to be an experienced rider ")
    print("you can either select Cruiser or Tourer")
    choice = input("what do you select:")

    if choice == "Cruiser":
        print("congratulations you won Goldwing")
    elif choice == "Tourer":
        print("congratulations you won BMW 1300 GS")
    else:
        print("you should quit riding now.")

def tooold():
    print("It's time for you to put your boots down and relax")

def underage():
    print("you need to be of a legal age")

def nakedbikes():
    print("This is an interesting choice i think you like long commutes")
    print("Which manufacturer do you want to go with Yamaha, KTM or Ducati")

    choice = input("Specify your choice manufacturer")

    if choice == "Yamaha":
        print("The best bike for you is Yamaha XSR 900")
    elif choice == "KTM":
        print("your dream bike should be KTM Super duke 1290")
    else:
        print("Bro Ducati Diavil is the bike to go for")

def sportsbike():
    print("so you like track riding eh!!")
    
    choice = input("Which bike do you want supersport, superbike or 250s")

    if choice == "supersport":
        print("Congrats you have selected the best bike possible, YAMAHA YZF R6")
    elif choice == "superbike":
        print("only buy this if you are willling to go to track, YAMAHA YZF R1")
    else:
        print("CBR 250 should be your starting bike")

def caferacer():
    print("You evil genius. Go way to go about your custom bike.")




start()

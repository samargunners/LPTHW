from sys import argv

script, first, second, third = argv

print(">>> argv=", repr(argv))

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

print(f"{first} {second} {third}")

yourname = input()

print(f"See I told you I could get your name correct: {yourname} ")
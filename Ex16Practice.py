from sys import argv

script, filename = argv

print(f"We're going to earse {filename}.") #here i am referring to the file i want to change
print("If you don't want that, hit CTRL-C (^C).") #this command line is to discribe the action
print("If you do want that, hit RETURN.")#this are the inbuild functions of python.

input ("?") #i need to understand what this is

print("Opening the file...") #this line says something.
target = open(filename, 'w') #this line give command to write a new file.

print("Truncating the file. Goodbye!")
target.truncate() #this command says the computer to go to the start of the file.

print("Now I'm going to ask you for three lines.") #this command asks us to give details that we want to enter in the file.

line1 = input ("Line 1: ")
line2 = input ("Line 2: ")
line3 = input ("line 3: ")

print ("I'm going to write these to the file") #this command explains what is it going to do next

target.write("{0}\n{1}\n{2}\n".format(line1,line2,line3))

print("And finally, we will close it.")
target.close() #always and always close files.

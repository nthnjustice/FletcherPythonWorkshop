# Session 2

##############################################################################
# Review variables

# What is a variable?
# What are the most common variable types?
# What limitations exist when using variables of different types?
# Why are meaningful names important when using variables?
##############################################################################
# Review print statements
# Challenge

firstName = "Nathan"
lastName = "Justice"

fullName = firstName + lastName

print("My name is ", fullName)
print("My name is " = fullName)
##############################################################################
# Review User-input, type-casting, and Conditionals
# Demo

userNumber = int(input("Give me a number between 1 and 10"))

if userNumber > 1 and userNumber < 10:
	print("You did it!")
else:
	print("Nope")

if userNumber > 1:
	if userNumber < 10:
		print("You did it!")
	else:
		print("The number is not less than 10")
else:
	print("The number is not greater than 1")
##############################################################################
# Challenge

# Take three numbers from the user, print the largest number

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if num1 > num2 and num1 > num2:
	print(num1, "is the largest.")
elif num2 > num1 and num2 > num3:
	print(num2, "is the largest.")
else:
	print(num3, "is the largest.")
##############################################################################
# introduce %

print(5/2)

print(5%2)

number = int(input("Provide a number: "))

i = 1

print("The even numbers between 1 and", number, " are:")

while i != number:
    if i%2 == 0:
        print(i)

    i = i + 1
    # i += 1
##############################################################################
# Lists

myList = [3, 5, 7]

print myList

myList[4] = 10

print myList

myList.append(9)

print myList

print myList[2]

myList.insert(3, 8) #index, value

print myList

myList.remove(7) #removes first element with value

print myList

myList.pop(2) #removes element at given index

print myList

print myList.index(9) #returns index for given element

print myList.count(5) #returns # of times a given element appears 

myList.sort() #no return value, sorts behind the scenes 

print myList #prints sorted list

myList.reverse() #no return value, reverses behind the scenes

print myList
numbers = len(myList)
print numbers
##############################################################################
# For-loops

roster = ["Pedro", "Anita" "Do", "Isabella", "Estelle"]

print(roster)
# How do you print one name at a time?

for name in roster:
	print(i)

# How do you print the names in alphabetical order?

numbers = [2, 8, 99, 4, 10, 0, 3, "I'm a string"]

lessThanFive = 0
greaterThanFive = 0

for i in numbers:
	if i < 5:
		lessThanFive += 1
	elif i > 5: # WHY NOT USE ELSE??
		greaterThanFive += 1

print(lessThanFive)
print(greaterThanFive)
##############################################################################
# Strings as lists

firstName = input("First name: ")
lastName = input("Last name: ")

print("Your initials are:", firstName[0] + lastName[0])
##############################################################################
# Reading in files

# Download addThis.txt

f = open("addThis.txt", "r")

total = 0

for line in f:
    total += int(line)

print(total)

f.close()

# Download LApolitics.txt

f = open("LApolitics.txt", "r")

first = f.readline()
second = f.readline()

print(first)
print(second)

for line in f:
    print(line)

print(f.readline())

f.close()

# Sort the LApolitics class and write to a new text file

f = open("LApolitics.txt", "r")

newList = []

for line in f:
    newList.append(line)

print(newList)

cleanList = []

f.close()
f = open("LApolitics.txt", "r")

for line in f:
    cleanList.append(line.strip())

print(cleanList)

cleanList.sort()

print(cleanList)

f.close()

newFile = open("LApoliticsSORTED.txt", "w")

#newFile.write(cleanList) # ERROR

for i in cleanList:
    newFile.write(i)

newFile.close() # You have to have this!

# Add the new line

for i in cleanList:
    newFile.write(i + '\n')
##############################################################################
# GC content problem

f = open("geneSequence.txt", "r")

sequence = f.read()

print(sequence)

gc = 0

for i in sequence:
    if i == "G" or i == "C":
        gc += 1

gcContent = gc/len(sequence) * 100

print("GC content = " + str(gcContent)[0:5] + "%")

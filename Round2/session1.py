# Introductions and interests
# My goals:
	# To help teach a useful skill
	# Remove the programming stigma (it's for everyone!)
	# Teach the terminology so you can speak the lingo
	# Teach problem solving skills
	# Show the webpage
# Introduction to programming in Python
	# What is it? What can I do with it?
	# Python 2.x vs. 3.x
		# Significant, but not vast, differences
		# Python 3 released in: December 3, 2008
		# Using Python 3.x because:
			# More long-term stability
			# No more updates for 2.x
		# Beware of version differences when looking at other people's code
			# No backwards compatability
		# http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
	# Learning a programming language is like learning a foreign spoken language
		# Special vocabulary and syntax
		# We all have the capacity to learn, practice makes perfect
# Download IDLE
	# IDLE basics
		# Open the software
		# What is the Interpreter and shell?
# Getting help
	# Google is your friend!
	# Don't reinvent the wheel
	# Python is popular - TONS of resources!
	# https://www.python.org/
	# Documentation - just check version!
		# https://docs.python.org/3/whatsnew/3.0.html
# Arithmetic using the shell
	# Addition
	# Subtraction
	# Multiplication
	# Division
		# Difference between Python 2.x and 3.x
			# 3 / 2 = 1.5
			# 3 // 2 = 1
			# 3 / 2.0 = 1.5
			# 3 // 2.0 = 1.0
	# Exponents 
# Making Python scripts
	# How to open a new scripts
	# How to progam a script
		# WHITESPACE MATTERS
	# Where to save the script
	# How to run the script
# Variables
	# What is a variable?
	# Why are they important?
	# Variable types
	# Using variables in the shell

# Python programming...

##############################################################################
'''
a = 123

b = 122

print(a) # PRINTING in Python 2.x
print(b)

print(a + b)

c = a + b

print(c)

'''
##############################################################################
'''
x = 12345
print(x)

x = 6789
print(x)

'''
##############################################################################
'''

a = 1.5

print(a * 2)

'''
##############################################################################
'''

x = 3 ** 2

print(x)

'''
##############################################################################
'''

x = 2 + 8 * 2

print(x)

x = (2 + 8) * 2

print(x)

'''
##############################################################################
'''

If you type like this, your code won't work.

It's important to annotate your code - for your future self and for others!

Comments allow you to do this without breaking your script.

# This is a comment. 
# Comments are ignored by the Interpreter

'''
##############################################################################
'''

# comments can occupy a line of their own

print(5) # comments can also be in-line


# You can use block comments
#for large amounts of text
#that span multiple lines

'''
##############################################################################
'''

# Variable types

a = 3
b = 1.5
c = "Hello"
d = 'World'

print(a)
print(b)
print(c)
print(d)

e = 1
print(a + e)

f = 1.5
print(b + f)

print(a + b)

print("BYE")

g = c + "BYE"
print(g)

print(c + "BYE")

h = c + d

print(h)

i = a + c
print(i)

j = b + d
print(j)

print(c + g + h + d) # Can you guess what this will print?

'''
##############################################################################

##############################################################################
'''

firstWord = "Hello" # notice camelCase syntax, first_word is another good option
secondWord = "World"

print(firstWord + secondWord)

print(firstWord + " " + secondWord)

phrase = "A good first program is to write" + " " + firstWord + " " + secondWord
print(phrase)

phrase = "A good first program is to write " + firstWord + " " + secondWord
print(phrase)

firstWord = "Hello "
midWord = " there "
secondWord = "World"
phrase = firstWord + midWord + secondWord
print(phrase) # difficult to manage

print(firstWord, midWord, secondWord)

print("My output is:", firstWord, secondWord) # can you guess the output?

'''
##############################################################################
'''

num = 5
word = "Hello"

print(num + word)

print(num, word)

'''
##############################################################################
'''

# notice how print statements create new lines

print("My name is")
print("Nathan")

# another example

print("My name is")
name = "Nathan"
print(name)

# if our print statement is limited to the order of the code, we can modify print endings

print("My name is", end=" ")
name = "Nathan"
print(name)

print("The World is", end=" happy ")
print("today.")

# We can manually insert new lines

print("I want a few new lines")
print()
print()
print()
print("Thank you")

# Choose how to separate arguments

a = "I"
b = "Feel"
c = "Pretty"

print(a, b, c)

print(a, b, c, sep="~~~")

print(a, b, c, sep="~~~", end="!!!!")

'''
##############################################################################
# Review variables
	# What is a variable?
	# How do they work?
	# Why are they important?
	# How do we use them?
		# Declare, assign value
	# What are some of the important variable types?
	# What limitations exist with variable types?
# The importance of naming your variables wisely
	# Don't use a, b, c, x, y, z
	# Use meaningful names
	# I will use meaningless names for convenience and teaching purposes only
##############################################################################
'''
# Conditionals - Boolean Logic

a = 3
b = 1

if a == 3:
	print("a is equal to 3")

#~

if a == 2:
	print("a is equal to 2")

#~

if a == 3:
	print("Here")
	print("We")
print("Go")

#~

if a == 2:
	print("Here")
	print("We")
print("Go")

#~ 

if b < a:
	print("b is less than a")

#~

if a < b:
	print("b is less than a")
elif b < a:
	print("a is less than b")

#~

if a < 3:
	print("a is less than 3")
elif a <= 3:
	print("a is less than or equal to 3")

#~ 

if a < 3:
  print("a is less than 3")
elif a == b:
  print("a is equal to b")
else:
  print("a is not less than 3 nor equal to b")

 #~

'''
##############################################################################
'''

num1 = 5
num2 = 7

if num1 == 5:
 	print("May the Force")
elif num2 == 7:
	print("Be with You")

#~

if num1 == 5:
	print("May the Force")
if num2 == 7:
	print("Be with You")

'''
##############################################################################
'''
# compound conditionals can be built using 'and' and 'or'
# 'and' requires both epressions to hold true
# 'or' needs a minimum of one of the expressions to hold true

a = 3
b = 1

if a > b and a == 3:
  print("a is greater than b and equal to 3")

if a > b or a == b:
  print("a is either greater than b, equal to b, or both")

'''
###########################################################################
'''

# What will this print?

a = 3
b = 1

if a > b and a != b:
  a = 5
else:
  print("1")

if a != 5 or a == 5:
  a = b
elif a > b:
  b = 7
else:
  print("2")

if a == b and a > 2:
  print "3"
elif a > 0 and b > 0:
  b = a
else:
  print("4")

if a != b or a != 0:
  print("5")
else:
  a = 5
  b = 3

if a > b:
  print("6")
else:
  print("7")

'''
###########################################################################
'''

data = input()

print(data)

data = input("Gimme data: ")

print(data)

number = input("Gimme a number: ")

print(number + 5)

'''
###########################################################################
'''

x = 5
word = "A number "

print(word + x)

x = str(x)

print(word + x)

sequence = 12345
sequence2 = "abcd"

aNiceString = str(sequence) + sequence2

print(aNiceString)

number = input("Gimme a number: ")
number = int(number)
print(number * 2)

number = int(input("Gimme a number: ")) * 2
print(number)

'''
###########################################################################
'''

# while-loops

# describe the features and behavior

i = 0

while i < 0:
	print("Looping...")
	i = i + 1

# COUNTDOWN project

'''
###########################################################################

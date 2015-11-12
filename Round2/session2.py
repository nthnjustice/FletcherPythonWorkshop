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
# This session will cover:
	# Conditional statements
	# User-input
	# Variable type-casting
	# While-loops
	# Countdown project

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

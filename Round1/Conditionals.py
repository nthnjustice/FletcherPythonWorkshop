a = 3
b = 1

if a == 3:
  print "a is equal to 3" #this statement will print

###########################################################################

a = 3
b = 1

if a < 3:
  print "a is less than 3" #this statement will NOT print
elif a <= 3:
  print "a is less than or equal to 3" #this statement will print

###########################################################################

a = 3
b = 1

if a < 3:
  print "a is less than 3" #this statement will NOT print
elif a == b:
  print "a is equal to b" #this statement will NOT print
else:
  print "a is not less than 3 nor equal to b" #this statement will print

###########################################################################

a = 3
b = 1

if a == 3:
  print "a is equal to 3" #this statement will print
elif a == 1:
  print "a is equal to 1" #this statement will NOT print
elif a == b:
  print "a is equal to b" #this statement will NOT print
else:
  print "a is not equal to 3 nor 1" #this statement will NOT print

###########################################################################

a = 3
b = 1

if a > b:
  print "a is greater than b" #this statement will print
if b < a:
  print "b is less than a" #this statement will ALSO print

#an 'if' statement can't have a parent 'if' statement
#all if statements will run regardless of their order or arrangement relative
  #to other conditional statements

###########################################################################

#compound conditionals can be built using 'and' and 'or'
#'and' requires both epressions to hold true
#'or' needs a minimum of one of the expressions to hold true

a = 3
b = 1

if a > b and a == 3:
  print "a is greater than b and equal to 3" #this statement will print

if a > b or a == b:
  print "a is either greater than b, equal to b, or both" #this will print

###########################################################################

a = 3
b = 1

if a > b and a != b:
  a = 5
else:
  print "1"

if a != 5 or a == 5:
  a = b
elif a > b:
  b = 7
else:
  print "2"

if a == b and a > 2:
  print "3"
elif a > 0 and b > 0:
  b = a
else:
  print "4"

if a != b or a != 0:
  print "5"
else:
  a = 5
  b = 3

if a > b:
  print "6"
else:
  print "7"

#what will this print? - answer below:


































#5
#7

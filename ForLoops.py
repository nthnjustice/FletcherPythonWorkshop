##import random
from random import randrange
var = 50
data = []

while var > 0:
  data.append(randrange(0, 100))
  var -= 1

print data

var = 0

print "While-loop"
while var < len(data):
  print data[var]
  var += 1

print "For-loop"
for element in data:
  print element

data[49] = 'Changed value'

for i in data:
  print i

#alternative for-loop approach
for i in range(0,len(data)):
  print data[i]

####  Syntax:
####    def function_name(parameter1, parameter_n):
####      Your Code Goes Here
##
def adder(some_num, some_other_num):
  '''This adds two integers together'''
  total = some_num + some_other_num
  return total

def subber(some_num, some_other_num):
  '''This subtracts two integers'''
  diff = some_num - some_other_num
  return diff

num1 = 5
num2 = 3

var = adder(num1, num2)

##print var
##
##print adder(3, 2)
##
##print subber(num1, num2)
##
##print subber(num2, num1)
####
##x = 10
##y = 7
##
##print adder(x, y)
##
##print adder(x/2, y+1)
##
##print adder(subber(2,1),adder(3,4))

##
def keyPrinter(dictionary):
  #Label the list
  print 'Keys -',
  #Print all the keys in the dictionary
  for i in dictionary:
    print i,
  #New Line
  print

def valuePrinter(dictionary):

  #Label the list
  print 'Values -',
  #Print all the values in the dictionary
  for i in dictionary:
    print dictionary[i],
  #New Line
  print

def printAll(dictionary):
  '''Will Call KeyPrinter and ValuePrinter on dictionary'''
  #Call KeyPrinter on dictionary
  keyPrinter(dictionary)
  #Call ValuePrinter on dictionary
  valuePrinter(dictionary)

def aestheticPrinting(dictionary):
  for i in dictionary:
    print i,dictionary[i],
  print
grades = {'Nii-Ofei':'A+', 'Pat':'B+', 'Akshay':'F'}

keyPrinter(grades)
valuePrinter(grades)


printAll(grades)
aestheticPrinting(grades)

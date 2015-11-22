# Session 4

##############################################################################
# Review functions

##############################################################################
# Dictionaries

# What is a dictionary?
# How do dictionaries and lists differ?
	# key-value pairs
	# unordered
# Why are dictionaries useful

myDict = {"one":1, "two":2, "three":3}

print(myDict)

print(myDict["one"])

myDict["three"] = "A change"

print(myDict)

myDict["four"] = 4

print(myDict)

isIn = "two" in myDict

print(isIn)

if "three" in myDict:
    print("YEP!")

theKeys = myDict.keys()

print(theKeys)

for key in theKeys:
    print(key)

theValues = myDict.values()

print(theValues)

for value in theValues:
    print(value)

del myDict["four"]

print(myDict)

myDict.clear()

print(myDict)

del myDict

print(myDict)

##############################################################################

def buildDict(path):
    f = open(path, "r")

    tempDict = {}

    for line in f:
        tempDict[line.strip()] = f.readline().strip()

    return(tempDict)

cabinet = buildDict("cabinet.txt")

print(cabinet)

##############################################################################
# Modules and libraries

# What are they? 
# Why are they important?

# Save the following as library.py

def printHello():
    print("Hello World")

var = "~~~~~~~~~~~~~~~~~"

numbers = [1, 2, 3]

###

import library

library.printHello()

print(library.numbers)

###

from library import var, printHello

print(var)

printHello()

###

from library import *

print(var)

printHello()

print(numbers)

##############################################################################

import math

x = math.pow(5, 3)

print(x)

x = math.sqrt(x)

print(x)

aConstant = math.pi # Use IDLE's autofill feature

##############################################################################

from random import *

# Show info window feature

x = randint(0, 10)
print(x)

x = randrange(0, 10, 5)
print(x)

characters = ["H", "E", "L", "O", "ASDFASDF"]

x = choice(characters)
print(x)

shuffle(characters) # CHECK INFO WINDOW - returns NONE

print(characters)

# None is a variable type

var = None

print(var)

if var == None:
    print("It's none")

# What is it good for?

##############################################################################

# https://docs.python.org/3/library/statistics.html

import statistics
import random

data = []

for i in range(0, 1000, 1):
    data.append(random.randint(0, 9999))

print(data)

average = statistics.mean(data)
median = statistics.median(data)
std = statistics.stdev(data)
variance = statistics.variance(data)

print("Average:", average)
print("Median:", median)
print("Standard Deviation:", std)
print("Variance:", variance)

### MAKE THIS INTO A BETTER PROGRAM!
# Why might we want to do this?
# Modularity, organization, etc.

import statistics
import random

def generateData(size, maxValue):
    data = []

    for i in range(0, size, 1):
        data.append(random.randint(0, maxValue))

    return(data)

def basicStats(data):
    print("Average:", statistics.mean(data))
    print("Median:", statistics.median(data))
    print("Standard Deviation:", statistics.stdev(data))
    print("Variance:", statistics.variance(data))

def basicStatsDict(data):
    statsDict = {}

    statsDict["Average"] = statistics.mean(data)
    statsDict["Median"] = statistics.median(data)
    statsDict["Standard Deviation"] = statistics.stdev(data)
    statsDict["Variance"] = statistics.variance(data)

    return(statsDict)

someData = generateData(10, 100)
print(someData)

print(basicStats(someData))

someDataDict = basicStatsDict(someData)
print(someDataDict)

moreData = generateData(10, 100)
print(moreData)

moreDataDict = basicStatsDict(moreData)
print(moreDataDict)

# Check which data set has a lower average

if someDataDict["Average"] > moreDataDict["Average"]:
    print("someData has a higher average")
elif someDataDict["Average"] < moreDataDict["Average"]:
    print("moreData has a higher average")
else:
    print("both data sets have the same average")

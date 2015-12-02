# Session 5

##############################################################################

# Review Dictionaries

from populations import population

# determine how many countries are in the dictionary
def numKeys(dictionary):
    keys = dictionary.keys()
    total = len(keys)
    return(total)

# print the countries in the dictionary
def printDict(dictionary):
    keys = dictionary.keys()

    for i in keys:
        print(i)

# allow user to search if a country is in the dictionary
def inDictionary(dictionary):
    keyDesired = input("What key are you looking for? ")

    if keyDesired in dictionary:
        print(keyDesired, "is in the dictionary")
    else:
        print(keyDesired, "is NOT in the dictionary")

# get the population of a country
def findValue(dictionary):
    keyDesired = input("What key would you like the value for? ")
    value = dictionary[keyDesired]
    return(value)

# find the total population of all countries in the dictionary
def totalPop(dictionary):
    values = dictionary.values()
    total = sum(values)
    return(total)

# find the country with the lowest population
def findLowest(dictionary):
    keys = dictionary.keys()
    keys = list(keys)
    lowest = keys[0]

    for i in keys[1:]:
        if dictionary[i] < dictionary[lowest]:
            lowest = i

    lowestPair = (lowest, dictionary[lowest])
    return(lowestPair)
    
        

numCountries = numKeys(population)
print(numCountries)
    
printDict(population)

inDictionary(population)

pop = findValue(population)
print(pop)

totalPopulation = totalPop(population)
print(totalPopulation)

lowestPop = findLowest(population)
print(lowestPop)

lowestPop_country = lowestPop[0]
lowestPop_population = lowestPop[1]
print(lowestPop_country)
print(lowestPop_population)

# add Sweden (9828655) to the dictionary
# find the lowest population again

##############################################################################

# writing software

# create a new folder for the modules 
# dataSoftware
	# data
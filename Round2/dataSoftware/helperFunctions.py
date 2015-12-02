import random
import statistics

randomDataSets = []
loadedDataSets = []

randomDataSets_withStats = []
loadedDataSets_withStats = []

# takes user input for random data parameters
def generateDataMenu():
    numDatum = int(input("size of the data set: "))
    minimum = int(input("minimum value of the data: "))
    maximum = int(input("maximum value of the data: "))

    data = generateData(numDatum, minimum, maximum)
    randomDataSets.append(data)
    
# generate a random data set
def generateData(length, minVal, maxVal):
    data = []

    i = length

    while i > 0:
        randomDatum = random.randint(minVal, maxVal)
        data.append(randomDatum)
        i -= 1

    return(data)

# print all of the random data sets
def printRandomDataSets():
    for setNumber in range(0, len(randomDataSets), 1):
        for data in randomDataSets[setNumber]:
            print(data, end=",")

        print()
        print()

# load a user's data file
def loadData():
    path = input("what data file would you like to load: ")
    path = "data/" + path

    f = open(path, "r")
    data = f.read()
    data = data.split()
    
    convertedData = []
    for i in data:
        convertedData.append(int(i))

    loadedDataSets.append(convertedData)

    f.close()

# print all of the loaded data sets
def printLoadedDataSets():
    for setNumber in range(0, len(loadedDataSets), 1):
        for data in loadedDataSets[setNumber]:
            print(data, end=",")

        print()
        print()

# run statistical tests
def statAnalysisMenu():
    print("sl - run statistical tests on the loaded data sets")
    print("sr - run statistical tests on the random data sets")
    print()
    choice = input("what would you like to do: ")

    if choice == "sl":
        loadedStatTests()
    elif choice == "sr":
        randomStatTests()
    else:
        print()
        print("invalid option")
        print()
        statAnalysisMenu()

# build the stat test results for the random data sets
def randomStatTests():
    setNumber = 0
    tempDict = {}
    tempList = []
    
    for i in range(0, len(randomDataSets), 1):
        setNumber = "Set #" + str(i)
        tempDict["Data"] = randomDataSets[i]
        tempDict["Stats"] = doStats(randomDataSets[i])
        tempList.append(setNumber)
        tempList.append(tempDict)
        randomDataSets_withStats.append(tempList)
        print()
        print("Set #" + str(i))
        printStatResults(tempDict)
        tempList = []
        tempDict = dict()

# build the stat test results for the loaded data sets
def loadedStatTests():
    setNumber = 0
    tempDict = {}
    tempList = []
    
    for i in range(0, len(loadedDataSets), 1):
        setNumber = "Set #" + str(i)
        tempDict["Data"] = loadedDataSets[i]
        tempDict["Stats"] = doStats(loadedDataSets[i])
        tempList.append(setNumber)
        tempList.append(tempDict)
        loadedDataSets_withStats.append(tempList)
        print()
        print("Set #" + str(i))
        printStatResults(tempDict)
        tempList = []
        tempDict = dict()

# perform the statistical tests
def doStats(data):
    statResults = {}
    
    statResults["max"] = max(data)
    statResults["min"] = min(data)
    statResults["mean"] = statistics.mean(data)
    statResults["median"] = statistics.median(data)
    statResults["stdev"] = statistics.stdev(data)
    statResults["variance"] = statistics.variance(data)

    return(statResults)

def printStatResults(dictionary):
    for key in dictionary["Stats"]:
        print(key + ": " + str(dictionary["Stats"][key]))

# write the data and stat results to an output file
def writeTestsMenu():
    print()
    print("y - yes")
    print("n - no")
    print()
    choice = input("would you like to save these results: ")

    if choice == "y":
        writeTests()
    elif choice == "n":
        return()
    else:
        print("invalid option")
        writeTestsMenu()

def writeTests():
    f = open("data/testRestults", "w")

    f.write("Loaded Data Results: \n")
    f.write("\n")

    writeLoadedTestsHelper(f)

    f.write("Random Data Results: \n")
    f.write("\n")

    writeRandomTestsHelper(f)

    f.close()

def writeLoadedTestsHelper(f):
    for list_ in loadedDataSets_withStats:
        f.write(list_[0] + "\n")
        for key in list_[1]:
            f.write(key + "\n")
            if isinstance(list_[1][key], list) == True:
                for element in list_[1][key]:
                    f.write(str(element) + ", ")
                f.write("\n")
            else:
                statKeys = list_[1][key].keys()
                for test in statKeys:
                    f.write(test + ": " + str(list_[1][key][test]) + ", ")
                    f.write("\n")

        f.write("\n")
        f.write("\n")
                    
def writeRandomTestsHelper(f):
    for list_ in randomDataSets_withStats:
        f.write(list_[0] + "\n")
        for key in list_[1]:
            f.write(key + "\n")
            if isinstance(list_[1][key], list) == True:
                for element in list_[1][key]:
                    f.write(str(element) + ", ")
                f.write("\n")
            else:
                statKeys = list_[1][key].keys()
                for test in statKeys:
                    f.write(test + ": " + str(list_[1][key][test]) + ", ")
                    f.write("\n")

        f.write("\n")
        f.write("\n")

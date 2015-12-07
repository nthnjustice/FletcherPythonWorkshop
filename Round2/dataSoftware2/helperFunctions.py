import random
import statistics

randomDataSets = []
loadedDataSets = []

def generateDataMenu():
    numDatum = int(input("size of the data set: "))
    minimum = int(input("minimum value of the data: "))
    maximum = int(input("maximum value of the data: "))

    data = generateData(numDatum, minimum, maximum)
    randomDataSets.append(data)


def generateData(length, minVal, maxVal):
    data = []
    
    for i in range(0, length):
        randomNumber = random.randint(minVal, maxVal)
        data.append(randomNumber)

    return(data)

def printRandomDataSets():
    for setNumber in range(0, len(randomDataSets)):
        for data in randomDataSets[setNumber]:
            print(data, end=", ")
            
        print()
        print()

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


def printLoadedDataSets():
    for setNumber in range(0, len(loadedDataSets)):
        for data in loadedDataSets[setNumber]:
            print(data, end=", ")
            
        print()
        print()


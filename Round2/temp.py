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
    

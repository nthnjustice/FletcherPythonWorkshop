# Session 3

##############################################################################
# Review lists and for-loops

countries = []

totalCountries = int(input("How many countries do you have? "))

i = 0

while i < totalCountries:
	countries.append(input("Input country: "))
	i += 1

print(countries)

countries.sort()

print(countries)

for country in countries:
    print(country[0])

##############################################################################
# Find the sum of a list of numbers

numbers = [1, 2, 3, 4, 5]

total = 0

for num in numbers:
	total += num

print(total)

##############################################################################
# Find the average of a list of numbers

numbers = [1, 2, 3, 4, 5]

total = 0

for num in numbers:
	total += num

average = total/len(numbers)

print(average)

print(int(average))

##############################################################################
# String parsing

phrase = "Life gave me lemons."

print(phrase[0])
print(phrase[0:4])
print(phrase[4:])
print(phrase[:4])

uppercase = phrase.upper()

print(uppercase)

lowercase = phrase.lower()

print(lowercase)

aList = phrase.split()

print(aList)

aList = phrase.split('e')

print(aList)

##############################################################################
# GC content problem

f = open("geneSequence.txt", "r")

sequence = f.read()

print(sequence)

gc = 0

for i in sequence:
    if i == "G" or i == "C":
        gc += 1

gcContent = gc/len(sequence) * 100

print("GC content = " + str(gcContent)[0:5] + "%")

##############################################################################
# Functions

# What are they, and why are they important?
	# blackbox
	# modularity
# built-in
# user-defined

def timesTwo(number):
    result = number * 2
    return(result)

userInput = int(input("What number do you want to double? "))

doubled = timesTwo(userInput)

print(doubled)

##############################################################################

def printList(aList):
    for i in aList:
        print(i)

numbers = [1, 2, 3, 4, 5]

printList(numbers)

##############################################################################

def summation(aList):
    total = 0
    for i in aList:
        total += i

    print("The total is", total)

numbers = [1, 2, 3, 4, 5]

summation(numbers)

print(total) # variable scoping

print(sum(numbers))

##############################################################################
# Variable scoping

def printMe():
    somethingElse = "World"
    print(something, somethingElse)

something = "Hello"

printMe()

print(somethingElse)

##############################################################################
# Challenge - write a function that finds the average of a list of numbers

def average(numbers):
    total = 0
    for i in numbers:
        total += i

    result = total/len(numbers)

    return(result)

myNumbers = [1, 2, 3, 4, 5]

print(average(myNumbers))

###############################################################################

def readTextFile(path):
    f = open(path, "r")
    f = f.read()
    return(f)

def tweetLength(tweets, option):
    if option == "words":
        tweetList = tweets.split()
        return(len(tweetList))
    elif option == "characters":
        return(len(tweets))
    else:
        print("Invalid option for tweetLength()")

def findHashtags(tweets):
    hashtags = []
    tweetList = tweets.split()

    for word in tweetList:
        if word[0] == "#":
            hashtags.append(word)

    return(hashtags)

twitter1 = readTextFile("tweets1.txt")
twitter2 = readTextFile("tweets2.txt")

lengthOfTweets = tweetLength(twitter1, "words")
lengthOfTweets = tweetLength(twitter1, "characters")
lengthOfTweets = tweetLength(twitter1, "word")

hashtags1 = findHashtags(twitter1)
hashtags2 = findHashtags(twitter2)

###############################################################################

def readTextFile(path):
    f = open(path, "r")
    f = f.read()
    return(f)

def tweetLength(tweets, option):
    if option == "words":
        tweetList = tweets.split()
        return(len(tweetList))
    elif option == "characters":
        return(len(tweets))
    else:
        print("Invalid option for tweetLength()")

def findHashtags(tweets):
    hashtags = []
    tweetList = tweets.split()

    for word in tweetList:
        if word[0] == "#":
            hashtags.append(word)

    return(hashtags)

twitter1 = readTextFile("tweets1.txt")
twitter2 = readTextFile("tweets2.txt")

lengthOfTweets = tweetLength(twitter1, "words")
lengthOfTweets = tweetLength(twitter1, "characters")
lengthOfTweets = tweetLength(twitter1, "word")

hashtags1 = findHashtags(twitter1)
hashtags2 = findHashtags(twitter2)

twitter3 = readTextFile("tweets3.txt")

trumpTweets = []

trumpTweets.append(twitter3)

trumpTweets.append(tweetLength(twitter3, "words"))

trumpTweets.append(tweetLength(twitter3, "characters"))

trumpTweets.append(findHashtags(twitter3))

print(trumpTweets)

print(trumpTweets[1], trumpTweets[2], trumpTweets[3])

print(trumpTweets[3][0])

for hashtag in trumpTweets[3]:
    print(hashtag)

###############################################################################
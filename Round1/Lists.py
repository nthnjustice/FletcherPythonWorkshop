myList = [3, 5, 7]

print myList

myList[4] = 10

myList.append(9)

print myList

print myList[2]

myList.insert(3, 8) #index, value

print myList

myList.remove(7) #removes first element with value

print myList

myList.pop(2) #removes element at given index

print myList

print myList.index(9) #returns index for given element

print myList.count(5) #returns # of times a given element appears 

myList.sort() #no return value, sorts behind the scenes 

print myList #prints sorted list

myList.reverse() #no return value, reverses behind the scenes

print myList
numbers = len(myList)
print numbers

data = [5, 7, 3, 7, 100, 4324, 5]

i = 0 #iterator
total = 0

while i < len(data): #loops through each element of data, starting at index 0
  print "The data-vale: " + str(data[i]) #prints iterator index
  total += data[i] #indexes data element and adds to total
  print "Total: " + str(total) #prints total as the loop runs
  i += 1 #allows iterator to step through each index

length = len(data) #returns the number of elements in the list
print total/length #calculates average

##############################################################################

alternative solution
print sum(data)/len(data)


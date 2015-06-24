data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print data #prints a list with elements that are lists

print data[1] #prints the sublist == [4, 5, 6]

#print each of the sublists as a list
for i in data:
  print i 

for sublist in data:
  print "Here's my list: ",sublist
  print "Elements in my list:"
  for element in sublist:
    print element

for i in range(len(data)):
  print "Here's my list: ",data[i]
  print "Here's my index in the big list: ",i
  print "Elements in my sublist:"
  for j in range(len(data[i])):
    print "Here's my index in the sublist: ", j    
    print data[i][j]
  print "Finished printing list number",i  

#alternative for-loop approach
for i in range(len(data)):
  for j in range(len(data[i])):
    print data[i][j],
  print 

dictionary = {'Fall 2012':['Comp11', 'Bio13', 'Ec05', 'Phil01'], 'Spring 2013':['Bio14',                                                                                
  'Psy01', 'Comp15', 'Gis01']}

print dictionary #prints the entire dictionary

print dictionary['Fall 2012'] #prints the list of courses for the key

print dictionary['Fall 2012'][1] #prints Bio13

#print each dictionary key
for key in dictionary:
  print key

#print each dictionary value (as lists)
for value in dictionary:
  print dictionary[value]

#print each element in the list for Spring 2013
for value in dictionary['Spring 2013']:
  print value

#print each element of all lists in the dictionary
for key in dictionary:
  for value in dictionary[key]:
    print value

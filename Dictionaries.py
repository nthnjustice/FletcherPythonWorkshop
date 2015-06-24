##dictionary = {key:value, key:value,...}
## Key must be string

dictionary = {'breakfast':'eggs', 'lunch':'hamburger', 'dinner':'pizza'}

print dictionary['breakfast'] #index with name of key

#print dictionary['eggs'] #error, can't index with value

dictionary['snack'] = 'apple'#mutable, can be dynamically updated

print dictionary

del dictionary['breakfast'] #removes a key and it's value

print dictionary

dictionary.clear() #empties the dictionary

print dictionary

del dictionary #deletes the entire dictionary

print dictionary

dictionary = {'Alice':1, 'Ben':2, 'Omar':3} #values can be of any type

print dictionary

dictionary['Jose'] = 4 

print dictionary

dictionary['Alice'] = 5 #all key names must be unique

print dictionary

dictionary['Julie'] = 2 #values don't have to be unique

print dictionary

  

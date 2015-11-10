tup1 = ('Nathan', 'Justice')

print tup1

tup2 = ('Alex',) #comma is needed for single-element tuples

print tup2

print tup1[1] #prints 'Justice'

#tup1[2] = 'val' #error, tuples are immutable and can't be updated

tup3 = ('Val',)

tup4 = tup1 + tup3 #builds the tuple ('Nathan', 'Justice', 'Val')

tup5 = tup4[0] + ' ' + tup4[2] + ' ' + tup4[1] 

print tup5

tup5 = (tup4[0], tup4[2], tup4[1]) #builds the tuple ('Nathan', 'Val', 'Justice')

print tup5



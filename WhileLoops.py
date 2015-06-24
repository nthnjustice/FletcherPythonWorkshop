#while-loop that counts down from 10 by 2

i = 10 #variable to determine number of iterations

while i > 0: #the condition may be whatever you want
    print i 
    i -= 2 #without this, the loop will be INFINITE

##############################################################################

#takes user input as a string and casts (converts) it to an integer
countdown = int(raw_input("What's the countdown? "))

print "Launch in..."

while countdown > 0:
    print countdown
    countdown -= 1

print "BLAST OFF!!!"

#get first number
#get operator
#get second number

repeat = "yes" #initialized so the while loop runs at start

while repeat.lower() == "yes": #runs again if the user wants, not case-sensitive

  var1 = int(raw_input("enter your first number: ")) #converted to integer
  cmd = raw_input("enter your operation: ")
  var2 = int(raw_input("enter your second number: ")) #converted to integer

  #compute

  if isinstance(var1, int) and isinstance(var2, int): #checks for "good-input"
    if cmd == "+":
      print var1 + var2
    elif cmd == "-":
      print var1 - var2
    elif cmd == "*":
      print var1 * var2
    elif cmd == "/":
      print var1 / var2
    else:
      print "Give us better input!"

  repeat = raw_input("Do you have another problem?") #allows user to use again

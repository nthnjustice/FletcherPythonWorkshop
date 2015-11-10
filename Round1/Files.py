#var = open(name_of_file, permissions)
#permissions can be r , r+, w, w+, wr, etc

#The variable is of type File

#Open a file called bio.txt, or create a new file called bio.txt
info = open('bio.txt', 'w+') #use w+ to permit writing

#Write to the file
info.write('My name is Nathan')  

info.close() #don't forget to close the file!

info = open('bio.txt', 'r+') #use r+ to permit reading

print info.read()

info.close() #don't forget to close the file!

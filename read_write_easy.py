# cheatsheet for opening, reading, writing, closing files
# python 2.x

print
print "Let's open and read a file.\ntexts/firstamendment.txt is available."
filename = raw_input("Type the filename: ")

f = open(filename)

print "We opened it. Now we will read it with a print statement.\n"

print f.read()

# return to the start of the file
f.seek(0)

# this will erase contents of the file specified:
t = open("target.txt", 'w')

t.write(f.read())

print "We also wrote the contents of the file into \"target.txt\"."

f.close()
t.close()

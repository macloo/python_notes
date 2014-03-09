# test writing to, from file, from book: lp5e pp. 288-290
# data all becomes strings when we write to file
# NOTE use of eval() to reconstitute objects
# NOTE: normally we use pickle module instead of this method - see 
# useful_modules.py for example of pickle

X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

# write those all into a file
F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

# what we see in the file (3 lines):
# Spam
# 43,44,45
# [1, 2, 3]${'a': 1, 'b': 2}

# now read that file, line by line
F = open('datafile.txt')
line = F.readline()
print line # adds a linespace (newline)
print line.rstrip() # doesn't

line = F.readline() # next line
print line # prints: 43,44,45
parts = line.split(',')
print parts # prints: ['43', '44', '45\n'] 

# convert them to numbers
print int(parts[0])
numbers = [int(P) for P in parts] # that's nice!
print numbers # prints: [43, 44, 45]

line = F.readline() # next line
print line # prints: [1, 2, 3]${'a': 1, 'b': 2} and a newline
parts = line.split('$')
print parts # prints: ['[1, 2, 3]', "{'a': 1, 'b': 2}\n"]
# note: split gave us a 2-item list
print eval(parts[0]) # prints: [1, 2, 3]
objects = [eval(P) for P in parts] # USEFUL
print objects
# prints: [[1, 2, 3], {'a': 1, 'b': 2}] - still a list

# test the dictionary object
newdict = objects[1]
print newdict # prints: {'a': 1, 'b': 2}
newdict['c'] = 99
print newdict # prints: {'a': 1, 'c': 99, 'b': 2}
# so it's really a functional dictionary! 

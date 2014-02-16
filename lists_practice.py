# some list operations:
# pop, extend, append, del, remove

fruits = ['apples', 'oranges', 'pears', 'apricots']

print
print "There are %d items in fruits." % len(fruits)
print

for fruit in fruits:
    print fruit

print 
print "First fruit:", fruits[0]
print "Fourth fruit:", fruits[3]

print
print fruits

fruits.pop()
print "pop:", fruits

fruits.extend(['plums', 'mangoes'])
print "extend:", fruits

fruits.append('bananas')
print "append:", fruits

del fruits[1]
fruits.remove('pears')
print

for fruit in fruits:
    print fruit

print
print "There are now %d items in fruits.\n" % len(fruits)

if "plums" in fruits:
    print "We have plums!\n"
else:
    print "There are no plums!\n"

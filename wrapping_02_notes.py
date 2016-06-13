# Wrapping Your Head Around Python notes
# https://www.sitepoint.com/premium/courses/wrapping-your-head-around-python-2916/

# lesson 2 notes - basics
from random import randint

# variables
thing1 = "desk"
thing2 = "chair"
thing3 = "lamp"
thing4 = "wastebasket"
group = thing1 + " " + thing2

print group

# if string1 is found in string2 - part of longer demo of if-elif-else
if thing3 in group:
	print "%s is there" % thing3
else:
	print "%s is not there" % thing3

#lists
mylist = [thing1, thing2, thing3]
print mylist
print mylist[1]

# append to list
print thing4
mylist.append(thing4)
print mylist
print len(mylist)

# remove from list
mylist.remove(thing1)
print mylist
print len(mylist)

#dictionaries - note that order is not fixed - unlike lists
prices = { thing1:500.00, thing2:225.00, thing3:42.75 }
print prices
print len(prices)

print thing4
print len(thing4)

# accessing values in a dict: use the name (name:value) not index
print prices[thing3]
print prices[thing1]
print prices["desk"]  # this works

# his while-loop example is bad - it would be better as a for-loop
# why do people do that?
# note - from random import randint - at top of file
# --- my while-loop ---
print "\nwhile-loop example with random numbers:"
health = 100
print "Health is %d." % health

while health > 0:
	threat = randint(0, 50)
	health = health - threat # or: health -= threat
	print "Threat = %d. Health is now %d." % (threat, health)
print "You're dead."
# that is a GOOD example because no one knows how long it needs to run


# for-loops
print "\nfor-loop with list:"

mylist = [thing1, thing2, thing3, thing4]
for thing in mylist:
	print thing

# with a dict - handy!
print "\nfor-loops with dict:\n(1)"

for key,value in prices.items():
	print key + " $" + str(value)

print "\n(2)"

for k in prices.keys():
	print k

print "\n(3)"

for v in prices.values():
	print v

# read/write files:
# "There is no difference between r and rt or w and wt since text mode is the default."
# http://stackoverflow.com/questions/23051062/open-files-in-rt-and-wt-modes
# see my file - read_write_easy.py

# demo of "for" loops, and a list, in Python (for beginners)

# -----------------------------------------------------------------------------
# for-loop 1

# print what the loop looks like in code
print "\nfor x in range(1, 5):"
print "    print x"

# this is that loop - now it will run
for x in range(1, 5):
    print x

# -----------------------------------------------------------------------------
# for-loop 2

# print what another loop looks like in code
print "\nfor x in range(5):"
print "    print x"

# this is that loop - now it will run
for x in range(5):
    print x

# -----------------------------------------------------------------------------
# create an empty list

print "\nNow you will type the names of several car brands, such as Ford.\n"

# create a new empty list, named cars
cars = []

# -----------------------------------------------------------------------------
# for-loop 3

# this loop asks you to populate that list with the names of 5 car brands
for x in range(0, 5):
    typed = raw_input("Type the name of a car brand: ")
    # this is how you add a new thing to a list
    cars.append(typed)
    print "Okay, you typed %s. That's %d of 5.\n" % ( cars[x], x + 1 )

print "This is the list object you created:"

# this prints the whole list object
print cars

print # blank line

# -----------------------------------------------------------------------------
# for-loop 4

print "A loop can do something with each thing in the list:"

# this for-loop prints each thing in the list named cars 
for car in cars:
    print car

print # blank line

# -----------------------------------------------------------------------------
# for-loop 5

print "Now we'll do exacty the same thing, but the loop looks "
print "a bit different this time. The output is the same:"

# this for-loop prints each thing in the list named cars 
for i in cars:
    print i

print # blank line

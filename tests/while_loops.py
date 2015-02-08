# compare for-loops and while-loops

# -----------------------------------------------------------------------------
# while-loop 1

print
print "First, we will run a simple while-loop:"

x = 0
while x < 5:
    print x, "hello"
    x += 1

# -----------------------------------------------------------------------------
# for-loop 1

print
print "Second, we will run a for-loop that produces the same output:"

for x in range(5):
    print x, "hello"

# -----------------------------------------------------------------------------
print
print "Look at the code. The while-loop above uses 4 lines, and the "
print "for-loop uses only 2 lines. So which is more efficient?"
print "Each loop produces exactly the same output, as you saw."
print
# -----------------------------------------------------------------------------
# create an empty list

print
print "Now you will type the names of several colors.\n"

# create a new empty list, named colors
colors = []

# -----------------------------------------------------------------------------
# while-loop 2

# this variable represents the user's answer to a question
answer = "y"

# this loop asks you to populate the list with the names of colors
while answer != "n":
    one_color = raw_input("Type the name of a color: ")
    # this is how you add a new thing to a list
    colors.append(one_color)
    print "Okay, you typed %s." % ( one_color ),
    answer = raw_input("Do you want to type another? n/y ")

print "\nThis is the list object you created:"

# this prints the whole list object
print colors

print # blank line

# -----------------------------------------------------------------------------
# while-loop 3

# this destroys the contents of the list as it prints each item in the list
# colors is True unless the list (colors) is empty 
# therefore, after all items have been popped off, the condition is False

while colors:
    x = colors.pop(0)
    print x

print # blank line
print "You should see all the colors you typed in a list above.\n"

# -----------------------------------------------------------------------------
# while-loop 4 -- similar to while-loop 3, but more efficient (compare them)

# this variable receives the user's answer to a question
answer = raw_input("Type the name of a color: ")

# this loop asks you to populate the list with the names of colors
# and checks when you want to quit - all in one line
while answer != "q":
    # this is how you add a new thing to a list
    colors.append(answer)
    print "You added %s to the list." % ( answer ), 
    answer = raw_input("Type another color, or type q to quit. ")


print "\nThis is the list object you created:"

# this prints the whole list object
print colors

print # blank line


# Python built-in functions
# Python for Kids, Briggs, chapter 9 
# python builtin_functions.py

# abs returns absolute value of a number - no negatives
print "abs() applied to 10 and to -10"
print "10:", abs(10)
print "-10:", abs(-10)
print

# bool returns False for 0 and True for all other numbers
print "bool() applied to 0 and to 25"
print "0:", bool(0)
print "25:", bool(25) 

# returns True for strings, False for "" or None
a = "Mindy"
b = ""
c = None
print "Mindy:", bool("Mindy"), '"":', bool(""), "None:", bool(None)
print

# lists, tuples, dictionaries/maps: returns False if empty, else True

# dir tells you which functions will work on a given value
print "dir()"
print dir("I am a string!")
print
"""
test = "I am a string!"
print dir(test)
print
print "Now see the help function (press q to quit help)."
raw_input()
help (test.upper)
"""

# eval converts a string to a Python expression so it will run -
# simple expressions only 
print "eval()"
calc = raw_input("Type a calculation, such as 100 / 4: ")
print eval(calc)
print

# exec is like eval, only it returns a value so you can store it
print "exec()"
calc = raw_input("Type a calculation, such as 100 / 4: ")
x = eval(calc)
print "%d + %d = %d" % (x, x, x + x)
print

# floats and ints
print "float() and int()"
y = 12
z = 3.658
print "%d becomes %f with float()" % (y, float(y))
print "%f becomes %d with int()" % (z, int(z))
print

# if you want to limit the float to 2 decimal places
print "%d becomes %.2f with float()" % (y, float(y))
print "%.2f becomes %d with int()" % (z, int(z))
print

# list of format strings - 
# http://docs.python.org/2/library/stdtypes.html#string-formatting-operations

# len gets the length in bytes for a string (or a file)
# or gets the number of items in a list, tuple, or dictionary/map

print "len()"
foo = "We will find out how many characters are in this string."
bar = foo.split(' ')
print "Length of sentence:", len(foo)
print "Length of list:", len(bar)

fruit_color = {"apple": "red",
            "banana": "yellow",
            "orange": "orange"
            }
print "Length of dictionary:", len(fruit_color)

nomor = ("satu", "dua", "tiga", "empat", "lima")
print "Length of tuple:", len(nomor)
print

# max and min return the largest/smallest item in a list, tuple, or string
print "max() and min()"

tuple1 = (3, 33, 2, 22, 8, 88, 6, 66)
print tuple1
print "The max is:", max(tuple1), "The min is:", min(tuple1)

print bar
print "The max is:", max(bar), "The min is:", min(bar)
print

# range used outside a for-statement
print "range()"

mylist = list(range(1, 6))
print mylist
print

mylist_step = (range(7, 63, 7))
for step in mylist_step:
    print step
print

# sum adds all numbers in a list or tuple, returns total
print "sum()"
print sum(tuple1)
print

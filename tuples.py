# use of tuples

thing1 = "desk"
thing2 = "chair"
thing3 = "lamp"

pricing1 = thing1 + " $" + "500.00"
pricing2 = thing2 + " $" + "250.00"
pricing3 = thing3 + " $" + "45.75"

# a list requires square brackets
prices = [ pricing1, pricing2, pricing3 ]

# x.split(";", 1)
# "if maxsplit is given, at most maxsplit number of splits occur, and the
# remainder of the string is returned as the final element of the list"
# "1" means "split once" - yields two parts
# of course itf there's only one semicolon, the "1" is unnecessary (optional)

new_price_list = []

for p in prices:
    a,b = p.split(" $", 1)
    print a
    print b
    # make a tuple and add it to the new list
    tuple1 = (a, b)
    print tuple1
    print tuple1[0]
    print tuple1[1]
    new_price_list.append(tuple1)
    print "---"

print new_price_list
print

# items in a tuple are accessed with indexes
# tuples are immutable - we cannot change their contents
# however, we CAN change the complete value of a tuple, like so:

tuple2 = ("foo", "bar", "foobar")
print tuple2
tuple2 = (2, 4, 6, 8)
print tuple2
# no errors - but we would get errors if we tried to change just one item
# in the tuple

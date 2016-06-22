# sometimes you don't want the plain vanilla arguments

def tip_helper(meal, tax, tipper = 20):
    tip = meal * tipper / 100
    total = meal + tax + tip
    return tip, total

a, b = tip_helper(40, 3.20)
print "Meal: $%.2f Tip: $%.2f" % (b, a)
# note that with the default of 20 provided for tipper, we can run the function
# with only 2 args even though it needs 3 - the 3rd is provided
# if we want a tip-percent other than 20, we can provide it

# %f is the formatter for floats and %.2f limits it to two decimal places

# if you need to accommodate an unknown number of arguments
inventory = {}
def show_inventory(cat, *toys):
    for toy in toys:
        inventory.update( {toy: cat} )
    return inventory

show_inventory("Ilsa", "catnip frog", "jingle bell")
print inventory
show_inventory("Truman", "yarn", "ball", "rubber mousie", "red ribbon")
print inventory

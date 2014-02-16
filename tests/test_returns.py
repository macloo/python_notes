# Exercise 21: Functions Can Return Something
# This should make returns more clear. 
"""
This is a test of a comment.
You can put in multi-line comments this way.
Even though they are not the comment color, they are okay.
"""

def function_1(a, b):
    print "Running function_1 ..."
    return a + b

def function_2(a, b):
    print "Running function_2, which has no return statement ..."
    x = a + b

x = function_1(5, 7)
print x

x = function_2(5, 7)
print x

x = function_1("dogs", "roses")
print x

x = function_2("dogs", "roses")
print x

# define two variables 
dogs = "Spot and Fluffy "
roses = "Fragrant Cloud and Buttercup 98"

x = function_1(dogs, roses)
print x

x = function_2(dogs, roses)
print x


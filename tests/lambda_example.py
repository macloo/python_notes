# the difference between a normal function definition ("f") and 
# a lambda function ("g") 
# http://www.secnetix.de/~olli/Python/lambda_functions.hawk
# http://stackoverflow.com/questions/890128/python-lambda-why  

# usual function
def f(x): 
	return x**2

print f(8)

# compare use of lambda to make an anonymous function
g = lambda x: x**2 # it will return this - don't use "return" keyword
# must fit all on one line 

print g(8)

"""
Note that the lambda definition does not include a "return" statement -- 
it always contains an expression which is returned. Also note that you can 
put a lambda definition anywhere a function is expected, and you don't have 
to assign it to a variable at all.
"""

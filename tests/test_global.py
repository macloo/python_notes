# test of global variables 

x = 5
print "x is assigned a value of 5"

def use_x1():
	# print x - this will throw an error: 
	# "UnboundLocalError: local variable 'x' referenced before assignment"
	x = 10
	print "x is assigned a value of 10 in function 1:"
	print  "x =", x, "(from function 1)"

def use_x2():
	global x
	print "global x is invoked in function 2."
	print "x = %d (from function 2)." % x
	x = x + 1
	print "Now x = %d (from function 2)." % x

print "x = %d outside functions" % x
use_x1()
print "x = %d outside functions, after function 1" % x
use_x2()
print "x = %d outside functions, after function 2" % x

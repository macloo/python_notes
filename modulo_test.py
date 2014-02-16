# testing for a prime number
# use of modulo
# use of try/except
# example of a for-loop with range
# learn about formatters:
# http://docs.python.org/2/library/stdtypes.html#string-formatting-operations

from sys import exit

print "\nWe will test a number to find out whether it is prime."
print "Try it with 25. Then try it with 7 or 13."
num = raw_input("Enter a number: ")

try:
    num = int(num)
except ValueError:
    print "That was not a number! Try again.\n"
    exit()

if num >= 100:
    print "Please enter a number that is less than 100.\n"
    exit()

for n in range(2, num):
	# below, % is the modulus sign
	# see http://learnpythonthehardway.org/book/ex3.html 
    
    remainder = num % n
    
    # below, %d is used to represent a variable 
    # some formatters, or format strings, are: %s %d %r
    # see http://learnpythonthehardway.org/book/ex5.html
    
    print "%d / %d leaves a remainder of %d" % (num, n, remainder)
    if remainder == 0:
        print "\nSorry, %d is not a prime number.\n" % num
        break
    elif n == num - 1:
        print "\nHooray! %d is a prime number." % num
        print "It cannot be divided by any number except 1 and itself.\n"

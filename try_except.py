# pattern for using try/except -- error handling
# https://docs.python.org/2/library/exceptions.html
# NOTE if there is NO ERROR, then the "try" statement just runs and
# "except" does not

# see this if you want to raise an exception -
# http://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python

print # blank line, because I like it

# throws an error because we can't concatenate integer and string
# x = 5 + "cheeseburger"

try:
    x = 5 + "cheeseburger"
# this catches ANY error
except Exception as e:
    print type(e) # use this to find the name of the type of error it is
    print e

print "\nAnother example:\n"

try:
    x = 5 + "cheeseburger"
# specify the kind of error if you know it or expect it
except TypeError as e:
    print e
finally:
    print 'The "finally" instructions execute no matter what.'
    print 'Having "finally" instructions is optional.'

print "\nAnd another example:\n"

try:
    y = 100 / 0
# specify the kind(s) of error if you know or expect them
except TypeError as e:
    print e
except ZeroDivisionError as e:
    print e
# we can have more than one "except" block, i.e. for two kinds of error
finally:
    print "finally ... foobar"

print "\nA less useful example:\n"

try:
    y = unknown_variable
# lacking specifics is allowed, but why would you?
except:
    print "There was an error."

print "\nAnother example:\n"

try:
    f = my_file.open()
# specific exception followed by "catch everything" exception
except IOError as e:
    print e
except Exception as e:
    print type(e) # find the name of the type of error it is
    print e

print

# format strings or formatters
# http://docs.python.org/2/library/stdtypes.html#string-formatting-operations

import math

print "\nThis is pi:", math.pi, "(nothing added)"
print
print "This is pi: %r (r)" % math.pi
print "This is pi: %f (f)" % math.pi
print "This is pi: %.2f (f truncated)" % math.pi
print "This is pi: %g (g)" % math.pi
print "This is pi: %d (d)" % math.pi
print

# example of %r output being very different from %s output
import datetime
x = datetime.date.today()
print x
print "Today's date is %s ..." % x
print "Today's date is %r ..." % x

print
a, b, c = "Truman", "brown", 12
print "The %s cat is %s, and he is %d years old." % (b, a, c)
print "The %r cat is %r, and he is %r years old.\n" % (b, a, c)

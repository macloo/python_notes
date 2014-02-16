# use of the "is" keyword 
'''
This keyword tests object identity; should NOT be used to test for string equality. It compares the memory address a object resides in.
'''
# http://bytes.com/topic/python/answers/523686-what-keyword

first = second = [0, 1, 2, 3]

print first
print second

print first is second # returns True or False

second[0] = 6

print first
print second

# above: objects using same space. below: different.
print "\nNext round:\n"

one = [0, 1, 2, 3]

two = [0, 1, 2, 3]

print one
print two

print one is two # returns True or False

two[0] = 6

print one
print two

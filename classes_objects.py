# people, then customers, which are also people
# from a tutorial at Sitepoint that is NOT very clear, but I can see how to
# assign attributes to a class, how to make an __init__ function, and sort of
# how two classes can work together
# https://www.sitepoint.com/premium/courses/wrapping-your-head-around-python-2916/

# name of a class should be capitalized
# https://www.python.org/dev/peps/pep-0008/#class-names

class Person:
    firstname = ""
    lastname = ""
    streetAddress = ""
    city = ""
    state = ""
    zipCode = ""

    # initialization function for this class
    def __init__(self, fname, lname, street, city, state, z):
        # assign those init parameters to the attributes
        self.firstname = fname
        self.lastname = lname
        self.streetAddress = street
        self.city = city
        self.state = state
        self.zipCode = z

    # example of a function for a class - see below for how to run it
    def printName(self):
        print "First name: %s Last name: %s" % (self.firstname, self.lastname)

# create a new instance of the class Person - __init__() is automatic
# see below for what happens if you don't include all the arguments
p001 = Person("Susan", "Smith", "123 Main St.", "Anytown", "Florida", "32123")

print # make a linespace for ease of use

# call an internal class function - on the instance p001 
p001.printName()

# create 3 more new instances of the class Person
p002 = Person("Mary", "Jones", "456 Spruce St.", "Footown", "Florida", "42123")
p003 = Person("Elizabeth", "Black", "789 Maple St.", "Bartown", "Florida", "52123")
p004 = Person("Kate", "White", "207 Oak St.", "Oldtown", "Florida", "62123")

# p005 = Person()
# TypeError: __init__() takes exactly 7 arguments (1 given)

# let's test those with 3 function calls
p004.printName()
p003.printName()
p002.printName()

# now define a NEW class, and pass in Person
# so a Customer is a Person also, but you can leave all the Person attributes
# blank - which seems not good to me, but ...
class Customer(Person):
    name = ""
    pickupLocation = ""

    # initialization function for this class
    # why return??
    # I took out the return and it makes no difference
    def __init__(self, name, pickupLocation, custID):
        self.name = name
        self.pickupLocation = pickupLocation
        self.__customerId = custID # see below
        # return

    def getPackage(self):
        return "Pickup for %s at %s Customer ID: %d" % (self.name,
            self.pickupLocation, self.__customerId)

    # with underscore, it is a private variable (not explained well in tutorial)
    # you can't access it in the same way - see below
    __customerId = 0

c001 = Customer("Jane Doe", "987 Walnut St.", 4790001)

# print c001.__customerId
# AttributeError: Customer instance has no attribute '__customerId'

print c001.getPackage()
# note that by using this internal function, we can see the __customerId

# as of now, this customer is a Person, but none of the Person attributes
# have been filled in
c001.printName()
# we can fill them in now - they exist but are empty
c001.firstname = "Jane"
c001.lastname = "Doe"
c001.streetAddress = "654 Main St."
c001.city = "Footown"
c001.state = "Ohio"
c001.zipCode = "34567"
# then run the Person function again and it will work
c001.printName()
# we have not changed any Customer attributes
print c001.getPackage()
print "%s, %s, %s %s" % (c001.streetAddress, c001.city, c001.state, c001.zipCode)
print c001.firstname
print c001.lastname
# note this one is from Customer, not Person
print c001.name

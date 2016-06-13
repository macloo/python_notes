# Wrapping Your Head Around Python notes
# https://www.sitepoint.com/premium/courses/wrapping-your-head-around-python-2916/

# lesson 2 notes - Step 7: Working with Strings

textfile = "Harry Potter, Gryffindor\n&Newt Scamander, Hufflepuff\n&Gilderoy Lockheart, Ravenclaw\n&Albus Dumbledore, Gryffindor\n&Severus Snape, Slytherin\n"
print textfile
print

houses = {}

newtext = textfile.split("&")
print newtext
# split transforms the single string into a list

# create a dictionary
for p in newtext:
    (a,b) = p.replace("\n", "").split(", ")
    houses[a] = b

print houses
print houses.keys()
print houses.values()

print
print houses["Harry Potter"]
print houses["Severus Snape"]

# some string searching to see if you typed an acceptable filename
# uses several string methods and expressions

import os.path

def check_bad_characters(filename):
    for c in filename[:-4]:
        if (not c.isalpha()):
            if (not c.isdigit()):
                if (c == " "):
                    badchar = "A space"
                elif (c == "_"):
                    badchar = None
                else:
                    badchar = c
                break
        else:
            badchar = None
    return badchar

def check_filename(filename):
    if (os.path.isfile(filename)):
        print "That filename already exists."
    elif (len(filename) > 20):
        print "%d characters is really too long for a" % len(filename),
        print "good filename!"
    elif (filename[-4:] != '.txt'):
        print "Your filename must end with .txt"
    elif (not filename[0].isalpha()):
	    print "A filename must begin with a letter."
    elif (badchar != None):
        print "Use only alphanumeric characters in filenames."
        print "%s is not acceptable." % badchar
    else:
        print "%s is an acceptable filename. Thanks!" % filename
        return filename
    return None

filename = None

while (not filename):
    try_filename = raw_input("What should the filename be? ")
    badchar = check_bad_characters(try_filename)
    filename = check_filename(try_filename)

print "Your filename is:", filename

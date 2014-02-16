# useful Python modules
# Python for Kids, Briggs, chapter 10 
# python useful_modules.py

import copy
import random
import time
import pickle

# copy - used to make a copy of an instance of an object
# Saves time if the object takes a lot of arguments

class Animal(object):
    def __init__(self, species, number_of_legs, color, mane_color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color
        self.mane_color = mane_color

flicka = Animal("horse", 4, "brown", "black")

black_beauty = copy.copy(flicka)
shadowfax = copy.copy(flicka)
black_beauty.color = "black"
shadowfax.color = "white"
shadowfax.mane_color = "white"
horses = [black_beauty, flicka, shadowfax]

print "\nExample of copy:"
for horse in horses:
    print "One horse is %s with a %s" % (horse.color, horse.mane_color),
    print "mane and tail."

# random - most useful functions are choice, randint, shuffle

print "\nPrint 10 random numbers:"
for i in range (0, 10):
    print random.randint(1, 100)

raw_input("Press any key to continue ...") # just pausing here

colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange', 
       'fuschia', 'teal', 'aquamarine', 'lavender']

print "\nPrint random words from a list:"
for i in range (0, 4):
    print random.choice(colors)

print "\nPrint all colors in alphabetical order:"
colors_in_order = sorted(colors)
for color in colors_in_order:
    print color

print "\nNow shuffle all the colors:"
random.shuffle(colors_in_order)
for color in colors_in_order:
    print color

raw_input("Press any key to continue ...") # just pausing here

# from sys import exit
# exit()
# I know this one

# time module
# this is the number of seconds since midnight on Jan. 1, 1970
# print time.time()

print "\nHere's an example that uses the time module:"

def setbomb():
    bomb_armed = True
    basetime = time.time()
    wire = random.choice(colors)
    
    print "\nYou open the top of the bomb case. The timer reads:"
    print "00:00:30"
    print "You'd better figure out how to defuse the bomb!"
    print "There are wires of many different colors. You can cut them."
    
    while bomb_armed:
        solve = raw_input("Which color do you want to try? ")
        if solve == wire:
            print "Whew! That fixed it! The timer has stopped!\n"
            bomb_armed = False
        else:
            bomb_armed = announce(basetime)

def announce(bt):
    nowtime = time.time()
    timeleft = 30 - (nowtime - bt)
    if timeleft > 0:
        print "\nThe bomb is still armed!"
        print "The timer reads:"
        if timeleft < 10:
            print "00:00:0%d" % timeleft
        else:
            print "00:00:%d" % timeleft
        return True
    else:
        print "\nToo late ..."
        print "KABOOM!!!"
        print "Goodbye!\n"
        return False

setbomb()

raw_input("Press any key to continue ...") # just pausing here

# time.asctime
print "\nHere is what we can print with asctime:"
print time.asctime()

tuple2 = (2008, 11, 4, 9, 30, 0, 1, 0, 0) 
# year, month, day, hour, minute, second, day of week, day of year, DST
print time.asctime(tuple2)

# time.localtime returns the current date and time as an object
# pp. 140-141 in Python for Kids 

# time.sleep
print "\nNow we will pause, with time.sleep:"

colors_in_order = sorted(colors)
for color in colors_in_order:
    print color
    time.sleep(1) # pauses for 1 second
print

# pickle can dump a dictionary into a file and later read it out again
# to save data from a game, for example

print "\nNow, some pickle magic (mostly invisible):"

raft_contents = ["compass", "map", "rope"]
location_items = ["raft"]
inventory = ["jerky", "machete"]

game_data = {'location': '03',
          'location_items': location_items,
          'raft_contents': raft_contents,
          'inventory': inventory
          }
save_file = open('save.dat', 'wb') # write in binary
pickle.dump(game_data, save_file)
save_file.close()

# now the contents of game_data are in the file save.dat
# next, we get the data out of that file

load_file = open('save.dat', 'rb') # read binary
restored_game_data = pickle.load(load_file)
load_file.close()
print
print restored_game_data


# fight an alien
# if-elif-else
# while loop
# two functions

from random import randint

# variables for the alien
alive = True
stamina = 10

def report(s):
    if s > 8:
        print "The alien is strong! It resists your pathetic attack!"
    elif s > 5:
        print "With a loud grunt, the alien stands firm."
    elif s > 3:
        print "Your attack seems to be having an effect! The alien stumbles!"
    elif s > 0:
        print "The alien is certain to fall soon! It staggers and reels!"
    else:
        print "That's it! The alien is finished!"

def fight(stam): # stamina 
    while stam:
        response = raw_input("> ")
        # fight scene
        if "hit" in response or "attack" in response:
            less = randint(0, stam)
            stam -= less # subtract random int from stamina 
            report(stam) # see above 
        elif "fight" in response:
            print "Fight how? You have no weapons, silly space traveler!"
        elif "run" in response:
            print "Sadly, there is nowhere to run.",
            print "The spaceship is not very big."
        else:
            print "\nThe alien zaps you with its powerful ray gun!"
            return True
    return False

# begin
print "\nA threatening alien wants to fight you!\n"

# call the function
# what it returns will affect the value of alive 
alive = fight(stamina)

if alive:
    print "\nThe alien lives on, and you, sadly, do not.\n"
else:
    print "\nThe alien has been vanquished. Good job!\n"

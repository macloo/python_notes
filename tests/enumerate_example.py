# get both list position and value from a list with "enumerate" 
# http://www.cyberciti.biz/faq/python-for-loop-examples-statements/

# a list of space shuttles 
shuttles = ['Columbia', 'Endeavour', 'Challenger', 'Discovery', 'Atlantis', 
         'Enterprise', 'Pathfinder']

# read shuttles list and enumerate it into index and value 
for index, value in enumerate(shuttles):
	print index, value


# https://www.udemy.com/game-development-fundamentals-with-python#/
# rewritten for Python 2.7
# plus some small mods

from sys import exit
from random import randint


class Main():
	"""
	In fact there's no need to write this as a class, because there is only 
	one class in the entire program. However, this is how it was done in 
	the tutorial.
	"""
	
	max_width = 5
	max_height = 5
	character_alive = True
	character_won = False
	monster_awake = False
	monster_awakened = False
	monster_move_per_turn = 2

	def __init__(self):
		self.reset_current_game()
		self.display_menu()

	def reset_current_game(self):
	# defaults for start_new_game()
		self.character_position = [0, 0]
		self.monster_position = [1, 1]
		self.trap_position = [0, 1]
		self.flask_position = [1, 0]

	def reset_all_settings(self):
	# used if you play again
		self.character_alive = True
		self.character_won = False
		self.monster_awake = False
		self.monster_awakened = False

	def place_character(self):
		self.character_position = [0, 0]

	def place_monster(self):
		self.monster_position = [randint(0, 4), randint(0, 4)]
		# ideally -
		# [randint(0, max_width - 1), randint(0, max_height - 1)]
		for i in ['character', 'trap', 'flask']:
			if (self.coordinate_collisions('monster', i)):
				self.place_monster() # do over

	def place_trap(self):
		self.trap_position = [randint(0, 4), randint(0, 4)]
		for i in ['character', 'monster', 'flask']:
			if (self.coordinate_collisions('trap', i)):
				self.place_trap()

	def place_flask(self):
		self.flask_position = [randint(0, 4), randint(0, 4)]
		for i in ['character', 'trap', 'monster']:
			if (self.coordinate_collisions('flask', i)):
				self.place_flask()

	def coordinate_collisions(self, coord1, coord2):
	# make sure a thing does not occupy an already occupied space
		if (coord1 == 'monster'):
			first = self.monster_position
		elif (coord1 == 'trap'):
			first = self.trap_position
		elif (coord1 == 'flask'):
			first = self.flask_position
		elif (coord1 == 'character'):
			first = self.character_position
		else:
			return None

		if (coord2 == 'monster'):
			second = self.monster_position
		elif (coord2 == 'trap'):
			second = self.trap_position
		elif (coord2 == 'flask'):
			second = self.flask_position
		elif (coord2 == 'character'):
			second = self.character_position
		else:
			return None

		if (coord1 == coord2):
			return None

		# compare coords of 2 things
		if (first[0] == second[0] and first[1] == second[1]):
			return True # they collide 
		else:
			return False

	def display_menu(self):
	# show a numbered menu of options for the player
		menu_list = ['Start New Game', '(Save Game)', '(Load Game)', \
		'Customize Setup', 'Exit']
		print "\nType the number of your choice.\n"
		for i in range(1, len(menu_list) + 1):
			print i, 
			print menu_list[i - 1]
		choice = raw_input("\nYour choice: ")
		self.menu_choice(choice)

	def start_new_game(self):
		self.reset_all_settings()
		self.reset_current_game()
		self.setup_game()

	def setup_game(self):
		self.place_character()
		self.place_monster()
		self.place_trap()
		self.place_flask()
		self.draw_grid()

	def menu_choice(self, choice):
	# respond to the player's menu choice
		try:
			choice = int(choice)
		except ValueError:
			choice = 0
		
		if (choice == 1):
			self.start_new_game()
		elif (choice == 2):
			pass
		elif (choice == 3):
			pass
		elif (choice == 4):
			pass
		elif (choice == 5):
			print "Goodbye!\n"
			exit()
		else:
			print "That wasn't a valid choice. Try again."
			self.display_menu()

	def collision_check(self):
	# this is for the character/player only, because it will be moved
		if (self.coordinate_collisions('character', 'monster')):
			self.character_alive = False
			return True
		elif (self.coordinate_collisions('character', 'flask')):
			self.character_won = True
			return True
		elif (self.coordinate_collisions('character', 'trap')):
			self.monster_awakened = True
			self.trap_position = [-1, -1] # off the grid
			return True
		return False # why not put in else? which is better?

	def check_boundary(self, new_x, new_y):
	# find out if player tried to go outside the grid
		min_width = 0
		min_height = 0
		if (new_x < min_width or new_x >= self.max_width or \
		new_y < min_height or new_y >= self.max_height):
			return False
		else:
			return True

	def player_move(self, choice):
	# execute the player's move, from draw_grid() function
		current_x = self.character_position[0]
		current_y = self.character_position[1]
		# up
		if(choice == 'w'): # using wasd instead of arrows
			if(not self.check_boundary(current_x, current_y - 1)):
				return False
			else:
				self.character_position = [current_x, current_y - 1]
				return True
		# left
		elif(choice == 'a'):
			if(not self.check_boundary(current_x - 1, current_y)):
				return False
			else:
				self.character_position = [current_x - 1, current_y]
				return True
		# down
		elif(choice == 's'):
			if(not self.check_boundary(current_x, current_y + 1)):
				return False
			else:
				self.character_position = [current_x, current_y + 1]
				return True
		# right
		elif(choice == 'd'):
			if(not self.check_boundary(current_x + 1, current_y)):
				return False
			else:
				self.character_position = [current_x + 1, current_y]
				return True
		else:
			return False

	def draw_grid(self):
		if (self.character_won):
			print "You have beaten the monster! Hooray!\n"
			choice = raw_input("Press any key to return to the menu or \
Return/Enter to exit.")
			if (choice):
				self.display_menu()

		elif (not self.character_alive):
			print "You have been eaten by the monster! Boo!\n"
			choice = raw_input("Press any key to return to the menu or \
Return/Enter to exit.")
			if (choice):
				self.display_menu()

		else:
			height = self.max_height
			width = self.max_width
			myrow = []
	
			for y in range(0, height):
				for x in range(0, width):
					if (self.monster_position[0] == x and \
					self.monster_position[1] == y and self.monster_awake):
						myrow.append('M')
					elif (self.character_position[0] == x and \
					self.character_position[1] == y):
						myrow.append('P')
					elif (self.trap_position[0] == x and \
					self.trap_position[1] == y):
						myrow.append('T')
					elif (self.flask_position[0] == x and \
					self.flask_position[1] == y):
						myrow.append('F')
					else:
						myrow.append('?')
				print ''.join(myrow)
				myrow = []
			print "Move using the w, a, s, and d keys."
			choice = raw_input("Move: ")
			if (not self.player_move(choice)):
				print "That's not a valid move."
				self.draw_grid() # function calls itself
			else:
				if (self.monster_awake):
					self.move_monster()
				if (self.collision_check()):
					if (self.monster_awakened): # only happens once
						self.monster_awake = True # this stays True
						print "You woke up the monster!"
						self.monster_awakened = False # this stays False
				self.draw_grid() # function calls itself

monster = Main()

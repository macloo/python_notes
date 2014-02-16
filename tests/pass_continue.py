# compare pass and continue keywords 
# http://www.tutorialspoint.com/python/python_loop_control.htm

print "\nExample of continue:\n"
# this will skip the letter "h" 
for letter in 'Python':
	if letter == 'h':
		continue
	print 'Current Letter:', letter

print "\nExample of pass:\n"
# prints each letter in "Python," skipping none
for letter in 'Python':
	if letter == 'h':
		pass
	print 'Current Letter:', letter

print "\nExample of break:\n"
# prints only the letters before "h" 
for letter in 'Python':
	if letter == 'h':
		break
	print 'Current Letter:', letter

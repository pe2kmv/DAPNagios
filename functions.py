# Convert string (True / False) to Boolean
# assume no case sensitive input
def StrToBool(s):
	s = s.capitalize()
	if s == 'True':
		return True
	if s == 'False':
		return False


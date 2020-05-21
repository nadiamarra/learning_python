import re

def is_valid_time(string):
	'''(string)--> bool
	Return True if the string is formatted correctly as a time (like 3:15 or 12:48).
	Return False otherwise or if the string contains anything else.

	>>>print(is_valid_time("10:45"))
	True
	>>>print(is_valid_time("1:23"))
	True
	>>>print(is_valid_time("10.45"))
	False
	>>>print(is_valid_time("1999"))
	False
	>>>print(is_valid_time("145:23"))
	False
	'''

	time_regex=re.compile(r'^\d{1,2}:\d{2}$')
	match=time_regex.search(string)
	if match:
		return True
	else:
		return False
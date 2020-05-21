import re

def parse_bytes(string):
	'''(string)--> list

	Return a list of the binary bytes contained in the string.
	Each byte is a combination of eight 1s or 0s.

	>>> parse_bytes("11010101 101 323")
	['11010101']
	>>> parse_bytes("my data is: 10101010 11100010")
	['10101010','11100010']
	>>> parse_bytes("asdsa")
	[]
	'''

	bytes_regex=re.compile(r'\b[01]{8}\b')
	match=bytes_regex.findall(string)
	return match
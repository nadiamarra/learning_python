import re

def parse_first_name(string): #calling group number
	name_regex=re.compile(r'(Miss|Mrs\.|Ms\.|Mr\.) ([A-Za-z]+) ([A-Za-z]+)')
	matches=name_regex.search(string)
	print(matches.group(2))

parse_first_name("Ms. Nadia Marra") 
#Nadia

def parse_name(string): #naming groups w/ ?P<name>
	name_regex=re.compile(r'(Miss|Mrs\.|Ms\.|Mr\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)')
	matches=name_regex.search(string)
	print(matches.group('first')) 
	print(matches.group('last'))

parse_name("Mr. Jack Phillips") 
#Jack
#Phillips

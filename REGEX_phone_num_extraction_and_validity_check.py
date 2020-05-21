import re

def extract_phone(input):
	phone_regex=re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match=phone_regex.search(input)
	if match:
		return match.group()
	else:
		return None

def extract_all_phones(input):
	phone_regex=re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

def is_valid_phone_v1(input):
	phone_regex=re.compile(r'^\b\d{3} \d{3}-\d{4}\b$')
	match=phone_regex.search(input)
	if match:
		return True
	else:
		return False

def is_valid_phone_v2(input):
	phone_regex=re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match=phone_regex.fullmatch(input)
	if match:
		return True
	else:
		return False

print(extract_phone("my number is 012 456-7890")) 
#012 456-78909
print(extract_phone("my number is 012 456-78909")) 
#None
print(extract_all_phones("my number is 012 456-7890 or call me at 789 456-1452"))
#['012 456-7890','789 456-1452']
print(extract_all_phones("my number is 012 456-7890 or call me at 789 456-14572"))
#['012 456-7890']
print(is_valid_phone_v1("012 456-7890")) 
#True
print(is_valid_phone_v1("012 456-7890 sdka")) 
#False
print(is_valid_phone_v2("012 456-7890")) 
#True
print(is_valid_phone_v2("012 456-7890 sdka")) 
#False	

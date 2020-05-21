import re

def parse_date(string):
	date_regex=re.compile(r'^(?P<day>[0-3]{1}[0-9]{1})(\/|\.|\,)(?P<month>[0-1]{1}[0-9]{1})(\/|\.|\,)(?P<year>(19|20)[0-9]{2})$')
	match=date_regex.search(string)
	if match:
		day=match.group('day')
		month=match.group('month')
		year=match.group('year')
		return {'d':day,'m':month,'y':year}

	else:
		return None


#Udemy solution
 
# def parse_date(input):  
#     pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
#     match = pattern.search(input)
#     if match:
#         return {
#             "d": match.group(1),
#             "m": match.group(2),
#             "y": match.group(3),
#         }
#     return None

print(parse_date("04,01,1984"))
#{'d':'12','m':'04','y':'2003'}
print(parse_date("03.09.1992"))
#{'d':'12','m':'11','y':'2003'}
print(parse_date("23/12/2008"))
#{'d':'12','m':'11','y':'2003'}
print(parse_date("12.11.200312"))
#None

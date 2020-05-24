#PART 1

def reverse_string(string):
	return string[::-1]

# print(reverse_string('awesome')) # emosewa
# print(reverse_string('Colt')) # tloC
# print(reverse_string('Elie')) # eilE

# SOLUTION
# def reverse_string(str):
#     s = ''
#     for i, char in enumerate(str[::-1]):
#         s += char
#     return s


def list_check(l): #returns True if each value in the list a a list
	result=[]
	for item in l:
		if type(item)==l: result.append(True)
		else: result.append(False)
	return all(result)

# print(list_check([[1,2,3],[8,9],[]])) #True
# print(list_check([[],[1],[2,3]])) # True
# print(list_check([[],[1],[2,3], (1,2)])) # False
# print(list_check([1, True, [],[1],[2,3]])) # False
# print(list_check([{},[],()])) #False
# print(list_check([{5:1},[5,6],(8,)])) #False

# SOLUTION
# return all(type(l) == list for l in vals)


def remove_every_other(l):
	new_l=[]
	for i, item in enumerate(l):
		if i%2==0:
			new_l.append(item)
	return new_l


# print(remove_every_other([1,2,3,4,5])) # [1,3,5] 
# print(remove_every_other([5,1,2,4,1])) # [5,2,1]
# print(remove_every_other([1])) # [1] 

# SOLUTION
# def remove_every_other(lst):
#     return [val for i,val in enumerate(lst) if i % 2 == 0]


def sum_pairs(l,num):
	for i in l:
		for y in l:
			if i!=y:
				s=i+y
				if s==num:
					return [i,y]
				else:
					return []

# print(sum_pairs([4,2,10,5,1], 6)) # [4,2]
# print(sum_pairs([11,20,4,2,1,5], 100)) # []

# SOLUTION
# def sum_pairs(ints, s):
#     already_visited = set()
#     for i in ints:
#         difference = s - i
#         if difference in already_visited:
#             return [difference, i]
#         already_visited.add(i)
#     return []


def vowel_count(string):
    string=string.lower()
    result={}
    for letter in string:
    	if letter in "aeiou":
    		count=string.count(letter)
    		result[letter]=count
    return result


# print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}
# print(vowel_count('Elie')) # {'e': 2, 'i': 1}
# print(vowel_count('Colt')) # {'o': 1}

# SOLUTION
# def vowel_count(string):
#     lower_s = string.lower()
#     return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}


#PART 2

def titleize(string):
	l=string.split()
	new_l=[]
	for word in l:
		initial=word[0].upper()
		rest=word[1:]
		word=initial+rest
		new_l.append(word)
	return " ".join(new_l)
	

# print(titleize('this is awesome')) # "This Is Awesome"
# print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"

# SOLUTION
# def titleize(string):
#     return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))


def find_factors(num):
	return [val for val in range(1,num+1) if num%val==0]

# print(find_factors(10)) # [1,2,5,10 ]
# print(find_factors(11)) # [1,11]
# print(find_factors(111)) # [1,3,37,111 ]
# print(find_factors(321421)) # [1,293,1097,321421 ]
# print(find_factors(412146)) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]

# SOLUTION
# def find_factors(num):
#     factors = []
#     i = 1
#     while(i <= num):
#         if (num % i == 0):
#             factors.append(i)
#         i += 1
#     return factors

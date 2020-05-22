import re

def censor(string):
	pattern=re.compile(r'\bfrack\w*\b',re.I)
	return pattern.sub("CENSORED", string)

print(censor("Frack you"))
print(censor("I hope you fracking die"))
print(censor("you fracking Frack"))

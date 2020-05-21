import re

url_regex=re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match=url_regex.search("http://www.youtube.com/videos")

print(match.group(0)) 
#http://www.youtube.com/videos
print(f"Protocol: {match.group(1)}") 
#Protocol: http
print(f"Domain: {match.group(2)}") 
#Domain: www.youtube.com
print(f"Everything else: {match.group(3)}") 
#Everything else: /videos
print(match.groups()) 
#('http', 'www.youtube.com', '/videos')

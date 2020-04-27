from keyword import iskeyword

def contains_keyword(*args):
    for string in args:
        if iskeyword(string): return True  #the first time we encounter a keyword, return True right away
    return False  #otherwise, once the loop is over return False 


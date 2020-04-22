def interleave(str1,str2):
    '''(string,string)->string
    Return a string with the two given strings zipped together.

    >>>interleave("hi","ha")
    "hhia"
    >>>interleave("aaa","zzz")
    "azazaz"
    >>>interleave("lzr","iad")
    "lizard"
    '''
    return "".join("".join(str) for str in zip(str1,str2))


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
    zipped_strings=list(zip(str1,str2))
    joined_tuples=["".join(str) for str in zipped_strings]
    return "".join(joined_tuples)


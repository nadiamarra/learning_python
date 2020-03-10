def count_consonants(s):
    '''str->(int)
    Return number of consonants in a string. Yy is included.
    >>>count_consonants("apple")
    3
    >>>count_consonants("string")
    5
    >>>count_consonants("aeiou")
    0
    '''

    num_cons=0
    for char in s:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            num_cons+=1
    return num_cons

def collect_consonants(s):
    '''str->(str)

    Return consonants in a string. Yy is included.

    >>>collect_consonants("apple")
    ppl
    >>>collect_consonants("string")
    strng
    >>>collect_consonants("aeiou")
    ''
    '''

    consonants=""
    for char in s:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonants=consonants+char    
    return consonants

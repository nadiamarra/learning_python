def up_to_vowel(s):

    '''(str)-> str

    Return a string until a vowel is found (not including the vowel).

    >>>up_to_vowel("ciaone")
    'c'
    >>>up_to_vowel("Brighton")
    'Br'
    >>>up_to_vowel("Trst")
    'Trst'
    '''


#we need an accumulator (otherwise we get substrings on different lines)
#we accumulate the substring to be returned in the accumulator

    #before_vowel=''

#we need to set the index to zero (starting position)
    #i=0

#we need to specify that the index must be inferior than the length of the string
#return value until the end of the string is reached (otherwise we get IndexError)
    #i<len(s)

#we need to say: retun value until it is a vowel
    #while not (s[i]) in "aeiouAEIOU":

#we need to add to the accumulator + the character at position i of string s
    #before_vowel+=s[i]

#we need to increment the index so that we can move on to the next character
    #i+=1

#return substring

    before_vowel=""
    i=0
    while i<len(s) and not (s[i]) in "aeiouAEIOU":
        before_vowel+=s[i]
        i+=1

    return before_vowel


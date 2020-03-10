def shift_left(L):

    '''(L)->NoneType

    Shift each item in L one position to the left and shift the first item to
    the last position.

    Precondition: len(L)>=1

    L=[a,b,c]
    shift_left(L) #list gets modified
    print(L)
    L=[b,c,a]

    '''
    first_item=L[0]
    
    for i in range(1,len(L)):
      L[i-1]=L[i]
    L[-1]=first_item
    


def count_adjacent(s):

    '''(str)-> num

    Return the number of occurrences of same adjacent letters.
    
    >>>count_adjacent("Marra")
    1
    >>>count_adjacent("Phillips")
    1
    >>>count_adjacent("Staffuzza")
    2
    '''

    #first I set a variable for the number of repeats to 0

    repeats=0
    
    #with a for loop, I iterate through the letters/indices of a given string
    #the range is the length of the string minus 1 (if I set just length of the
    #string, I will get an IndexError, because the last position of the string
    #can't be compared with the next index (there is no next index)

    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            repeats+=1
    return repeats
        
                   
    

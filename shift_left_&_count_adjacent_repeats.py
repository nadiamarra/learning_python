def shift_left(L):

    '''(list)->NoneType ##None is returned, the function modifies the initial list

    Shift each item in L one position to the left and shift the first item to
    the last position.

    Precondition: len(L)>=1

    L=["a","b","c"]
    shift_left(L) #list gets modified
    
    #if I print I get >L=["c","b","a"]
 

    '''
    first_item=L[0]   ##need this to keep track at the value at pos 0
    
    for i in range(1,len(L)): #from index 1 (want to move 'b' first) and until the end of the list
      L[i-1]=L[i]             #I move the item to the left
    L[-1]=first_item          #-1 is the last element of a list, we set that to our first_item variable
    


def count_adjacent_repeats(s):

    '''(str)-> num

    Return the number of occurrences of a character and an adjacent character being the same.
    
    >>>count_adjacent_repeats("Marra")
    1
    >>>count_adjacent_repeats("Phillips")
    1
    >>>count_adjacent_repeats("Staffuzza")
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
 
##    Alternative:           
##    for i in range(1,len(s)):
##        if s[i]==s[i-1]:
##            repeats+=1
##    return repeats
                   
    

def calculate_average(list):

    '''(list of list of [str,num])->float

    Return the average of at least two values in list.
    
    >>>calculate_average([['Nadia',160],['Jack',194],['Kicsi',50]])
    134.66
    >>>calculate_average([['Nadia',36],['Jack',27.5],['Kicsi',11.5]])
    25.0

    '''

    total=0

    for item in list:
        total=total+item[1]

    return total/len(list)
    
    
    

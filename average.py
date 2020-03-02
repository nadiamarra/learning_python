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
        total+=item[1]
    return total/len(list)
    
 


def averages(list):
    '''(list of list of number}->list of float

    Return a new list in which each item is the average of the grades
    in the inner list at the corresponding position of grades.
    
    >>>averages([[10,9,8],[2,4,3],[5,6,7]])
    [9.0,3.0,6.0]
    '''

    averages=[]

    for item in list:
        total=0
        for mark in item:
            total+=mark
        averages.append(total/len(item))
    return averages
    

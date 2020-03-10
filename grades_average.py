def calculate_average(assignment_grades):


    '''(list of lists[str, num])->float
    Return the average of grades in assignment_grades.
    
    >>>calculate_average([['Assig1',80],['Assig2',90]])
    85.0
    '''

    result=0

    for item in assignment_grades:
        result+=item[1]
    return result/len(assignment_grades)


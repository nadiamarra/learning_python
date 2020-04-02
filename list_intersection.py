def intersection(list1,list2):

    '''(list,list)->list

    Return a list given two lists with the values that are in both input lists.
    >>>intersection([1,2,3],[2,3,4])
    [2,3]
    >>>intersection(["a","z"],["x","y","z"])
    ["z"]
    '''
    new_list=[]
    
    for val in list1:
        if val in list2:
            new_list.append(val)
    return new_list
            


def intersection_v2(list1,list2):
    return [val for val in list1 if val in list2]

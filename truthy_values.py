def compact(lista):


    '''(list)->list

    Return a list of truthy values given a list with truthy and falsey values.

    compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
    '''


    return [val for val in lista if bool(val) is True]

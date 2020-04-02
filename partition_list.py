def isEven(num):
    return num % 2 == 0

def partition(lista,callback_function):

    '''(list,callback_function)->list of lists

    Return a truthy list and a falsy list inside a larger list given a list and a callback function.

    >>>partition([1,2,3,4], isEven)
    [[2,4],[1,3]]
    '''
    
    truthy_list=[]
    falsy_list=[]
    for num in lista:
        if isEven(num) == True:
            truthy_list.append(num)
        else:
            falsy_list.append(num)
    return [truthy_list,falsy_list]
                       
def partition_v2(lista,callback_function):
    truthy_list=[num for num in lista if isEven(num) is True]
    falsy_list=[num for num in lista if isEven(num) is False]
    return [truthy_list,falsy_list]

def partition_v3(lista,callback_function):
    return [[num for num in lista if isEven(num) is True],[num for num in lista if isEven(num) is False]]

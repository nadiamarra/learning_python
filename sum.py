def sum_items(list1, list2):
    '''(list of number, list of number)->list of number

    Return a new list in which each item is the sum of the items at the
    corresponding position of list1 and list2.

    Precondition: len(list1)==len(list2)

    >>>sum_items([1,2,3],[2,4,2])
    [3,6,5]
    '''

    sum_list=[]

    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])
    return sum_list


def sum_even_numbers(num1, num2):
    '''(num)-> num
    
    Return the sum of the even numbers.
    
    >>>sum_even_numbers(0,10)
    20
    '''
    
    total=0
    for num in range(num1,num2):
        if num%2==0:
            total+=num
    print(total)
    
    

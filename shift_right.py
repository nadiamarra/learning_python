def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1

    >>> shift_right([1,2,3])
    [3, 1, 2]
    '''

    last_item = L[-1]

    for i in range(1,len(L)):   #during the first iteration of the loop, i refers to 1, so len(L) -1 is the index of the last item in L
        L[len(L) - i] = L[len(L) - i - 1]        #as i increases, the indices move backwards through the list

    L[0] = last_item

    return L

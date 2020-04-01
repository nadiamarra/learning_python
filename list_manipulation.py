def list_manipulation(lista,command,location,value=0):

    '''
    list_manipulation([1,2,3], "remove", "end") # 3
    list_manipulation([1,2,3], "remove", "beginning") #  1
    list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
    list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
    '''
    
    if command=="add":
        if location=="beginning":
            lista.insert(0,value)
            return lista
        elif location=="end":
            lista.extend([value])
            return lista
    elif command=="remove":
        if location=="beginning":
            return lista.pop(0)
        elif location=="end":
            return lista.pop()
    
    

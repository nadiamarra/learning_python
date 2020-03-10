def inhospitable_weather(temp):
    ''' (number) -> bool
    Return True if and only if the given temperature in degrees Celsius is unpleasant (too hot or too cold).
    >>> inhospitable_weather(20)
    False
    '''
    return temp<12 or temp>28



##    return 12<temp>28



##    if temp > 28:
##        return True
##    elif temp < 12:
##        return True
##    else:
##        return False

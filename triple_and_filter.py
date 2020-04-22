def triple_and_filter_v1(num_list):  #with list comprehension
    return [num*3 for num in num_list if num%4==0]
    

def triple_and_filter_v2(num_list):   #with map and filter
    return list(filter(lambda x: x%4==0, map(lambda x: x*3, num_list)))

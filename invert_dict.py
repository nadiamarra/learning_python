fruit_to_colour={
    'banana':'yellow',
    'cherry':'red',
    'orange':'orange',
    'pear':'green',
    'peach':'orange',
    'plum':'purple',
    'pomegranate':'red',
    'strawberry':'red'
    }


#inverting fruit_to_colour 

colour_to_fruit={}                  #accumulator set as the new dict name

for fruit in fruit_to_colour:       #iterating over the keys
    colour=fruit_to_colour[fruit]   #assigning all the values to the variable colour

#adding to the new dict
    colour_to_fruit[colour]=fruit

    

###issue: there are more than one fruit for each of the colours associated
###with those three missing fruits
##
###if colour is not already a key in the accumulator
###add colour:[fruit] as an entry
##
##    if not(colour in colour_to_fruit):
##        colour_to_fruit[colour]=[fruit]
##
#####otherwise, append fruit to the existing list
##
##    else:
##        colour_to_fruit[colour].append(fruit)
##

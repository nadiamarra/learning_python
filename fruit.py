fruit_to_colour={'banana':'yellow','cherry':'red','orange':'orange','pear':'green','peach':'orange','plum':'purple','pomegranate':'red','strawberry':'red'}


#Invert fruit to colour (new dict: colours to fruits)


colour_to_fruit={}                  #accumulator

for fruit in fruit_to_colour:       #we iterate over the keys
    colour=fruit_to_colour[fruit]   #extract the colour
    

#issue: there are more than one fruit for each of the colours associated
#with those three missing fruits

#if colour is not already a key in the accumulator
#add colour:[fruit] as an entry

    if not(colour in colour_to_fruit):
        colour_to_fruit[colour]=[fruit]

###otherwise, append fruit to the existing list

    else:
        colour_to_fruit[colour].append(fruit)


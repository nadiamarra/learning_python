price=0
destinations={"H":50,"B":60,"F":70,"M":100}


destination=input("***Welcome to Nadia's Train Service.***\n***Where do you want to go?***\n\nPlease type: \nH for Hannover, \nB for Berlin, \nM for München \nF for Frankfurt :\n")
#\nQ for quitting the service
#while destination !="Q":

if destination in destinations:
    price=destinations[destination]

#calculating type of journey
    journey=input("\nType O for one-way or R for round-trip :\n")
    if journey=="R":
        price=price*2

#calculating passengers

    passengers=input("\nHow many passengers? :\n")
    price=price*int(passengers)

#calculating reduction

    reduction=input("\nPlease insert: \n0 if you don't have a BahnKarte, \n25 if you have a BahnKarte25, \n50 if you have a BahnKarte50:\n")
    discount=int(reduction)/100
    price=price-(price*discount)
    
    print(f"\n***Your ticket costs: €{price}***\n***Please transfer the amount to Nadia's bank NOW!***\n***Thanks, bye!***")

else:
    print("Sorry, we don't serve that city. Bye!")







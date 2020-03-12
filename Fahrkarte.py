price=0
destinations={"H":50,"B":60,"F":70,"M":100}
another=""
journey=""

print("\n***\U0001f600 Welcome to Nadia's Train Service \U0001f600***")
while another!="N":
    destination=input("\nWhere do you want to go?\n\nPlease type: \nH for Hannover, \nB for Berlin, \nM for München \nF for Frankfurt :\n")
    if destination in destinations:
        price+=destinations[destination]
        print(f"\nAmount in your basket €{price}")

#calculating type of journey
        journey=input("\nType O for one-way or R for round-trip:\n")
        while journey!="R" and journey!="O":
            print("Wrong input")
            journey=input("\nType O for one-way or R for round-trip:\n")
        if journey=="R":
            price=price*2
            print(f"\nAmount in your basket €{price}")
        elif journey=="O":
            print(f"\nAmount in your basket €{price}")
#calculating passengers

        passengers=input("\nHow many passengers? :\n")
        price=price*int(passengers)
        print(f"\nAmount in your basket €{price}")

#another ticket 
        another=input("\nDo you want to purchase another ticket? Y/N\n")
    
    else:
        print("\nSorry, we don't serve that city!")

#calculating reduction
reduction=input("\nPlease insert: \n0 if you don't have a BahnKarte, \n25 if you have a BahnKarte25, \n50 if you have a BahnKarte50:\n")
discount=int(reduction)/100
price=price-(price*discount)

print(f"\n***Total: €{price}***\n***Please transfer €{price} to Nadia's bank***\n***\U0001f600 Thank you for using Nadia's services. \U0001f600 Bye!***")



#summary= Your one-way ticket to Hannover costs...
#prices don't add up


#Berlin - O x 1 Bahncard 50 = 30 correct
#Berlin - R x 1 Bahncard 25 = 90 correct
#Berlin - R x 2 +  München - O x 1 Bahncard 50 = 170 correct

#Hannover - R x3 = 300
#München x R x 6 = 1200 
#Frankfurt x R  x2 = 280
#Frankfurt x 0 x 1 = 70
#bahncard 25 0 = 1387.5


#need to show intermediate calculations

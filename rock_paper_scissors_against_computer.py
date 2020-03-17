import random
player_wins=0
computer_wins=0

while player_wins<2 and computer_wins<2:
        print("rock...\npaper...\nscissors...")
        print(f"Player Score:{player_wins} Computer Score:{computer_wins}")
        player=input("Player, make your move: ")
        rand_num=random.randint(0,2)
        if rand_num==0:
                computer="rock"
        elif rand_num==1:
                computer="paper"
        else:
                computer="scissors"
        print(f"Computer plays {computer}")
        if player==computer:
                print("It's a tie!")
        elif player=="rock":
                if computer=="scissors":
                        print("Player wins!")
                        player_wins+=1
                elif computer=="paper":
                        print("Computer wins!")
                        computer_wins+=1
        elif player=="paper": 
                if computer=="rock":
                        print("Player wins!")
                        player_wins+=1
                elif computer=="scissors":
                        print("Computer wins!")
                        computer_wins+=1
        elif player=="scissors":
                if computer=="paper":
                        print("Player wins!")
                        player_wins+=1
                elif computer=="rock":
                        print("Computer wins!")
                        computer_wins+=1
        else:
                print("Something went wrong")
print(f"FINAL SCORES... Player:{player_wins} Computer:{computer_wins}")
if player_wins>computer_wins:
        print("Bravoooo")
else:
        print("Shit")
        

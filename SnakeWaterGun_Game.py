import random
print("Are you ready to play the Snake Water Gun Game? Let's Go!!!")
print("How to play? -> Enter 's' for Snake, 'w' for Water and 'g' for Gun. There will be 10 rounds of the game.")
name = input("Enter Your name to start: ")
comp_wins = 0
player_wins = 0
ties = 0
comp_list = ["snake", "water", "gun"]
rounds =  10
while(rounds):
    comp_choice = random.choice(comp_list)
    player_choice = input("Choose: Snake(s), Water(w) or Gun(g??? ")
    if player_choice=="s":
        if comp_choice=="snake":
            print("Computer chose",comp_choice)
            print("It's a Tie!!!")
            ties+=1
        elif comp_choice=="water":
            print("Computer chose",comp_choice)
            print(f"{name} Wins!!!")
            player_wins+=1
        elif comp_choice=="gun":
            print("Computer chose",comp_choice)
            print("Computer Wins!!!")
            comp_wins+=1
    elif player_choice=="w":
        if comp_choice=="snake":
            print("Computer chose",comp_choice)
            print("Computer Wins!!!")
            comp_wins+=1
        elif comp_choice=="water":
            print("Computer chose",comp_choice)
            print("It's a Tie!!!")
            ties+=1
        elif comp_choice=="gun":
            print("Computer chose",comp_choice)
            print(f"{name} Wins!!!")
            player_wins+=1
    elif player_choice=="g":
        if comp_choice=="snake":
            print("Computer chose",comp_choice)
            print(f"{name} Wins!!!")
            player_wins+=1
        elif comp_choice=="water":
            print("Computer chose",comp_choice)
            print("Computer Wins!!!")
            comp_wins+=1
        elif comp_choice=="gun":
            print("Computer chose",comp_choice)
            print("It's a Tie!!!")
            ties+=1
    rounds-=1
print("~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~ Leaderboard ~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~-_-~\n")
print("\t\tYour Wins\t\t\t\t     Computer Wins\t\t\t\t   Ties")
print("\t\t   ",player_wins,"\t\t\t\t\t\t  ",comp_wins,"\t\t\t\t\t   ",ties)
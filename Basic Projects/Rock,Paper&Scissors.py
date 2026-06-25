import random

#Global_Variables
choices = ("rock", "paper", "scissors")


#User_Inputs
def get_user_input():
    choice = input("Pick Your Choice?(\"rock\", \"paper\", \"scissors\"):")
    while choice not in choices:
        choice = input("Pick Your Choice?(\"rock\", \"paper\", \"scissors\"):")
    return choice
        

#Pc_input

def get_pc_input():
    pc_choice = random.choice(choices)
    print(f'PC choice was {pc_choice}')
    return pc_choice



#Comparisson and choosing winner

def determine_winner(user_input, pc_input):
    if user_input == pc_input:
        print("Draw!")
    elif (user_input == "rock" and pc_input == "scissorc") \
            or (user_input == "scissors" and pc_input == "paper") \
            or (user_input == "paper" and pc_input == "rock"):
        print("User Won!")
    else:
        print("PC Won!")



#getting the game go!!

def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input, pc_input)
    print("End Of The Game!")



#On_loop

respond = 'y'
while respond == "y":
    main()
    respond = input("Do you wanna play another round?(y/n):")












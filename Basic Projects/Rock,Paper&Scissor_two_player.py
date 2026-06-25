#Global_Variables
choices = ("rock", "paper", "scissors")


#User_Inputs
def get_first_player_input():
    first_choice = input("First Player Pick Your Choice?(\"rock\", \"paper\", \"scissors\"):")
    while first_choice not in choices:
        first_choice = input("Pick Your Choice?(\"rock\", \"paper\", \"scissors\"):")
    return first_choice
        

#Pc_input

def get_second_player_input():
    second_choice = input("Second Player Pick Your Choice?(\"rock\", \"paper\", \"scissors\"):")
    while second_choice not in choices:
        second_choice = input("Pick Your Choice?(\"rock\", \"paper\", \"scissors\"):")
    return second_choice



#Comparisson and choosing winner

def determine_winner(first_player_input, second_player_input):
    if first_player_input == second_player_input:
        print("Draw!")
    elif (first_player_input == "rock" and second_player_input == "scissorc") \
            or (first_player_input == "scissors" and second_player_input == "paper") \
            or (first_player_input == "paper" and second_player_input == "rock"):
        print("Fisrt Player Won!")
    else:
        print("Second Player Won!")



#getting the game go!!

def main():
    first_player_input = get_first_player_input()
    second_player_input = get_second_player_input()
    determine_winner(first_player_input, second_player_input)
    print("End Of The Game!")



#On_loop

respond = 'y'
while respond == "y":
    main()
    respond = input("Do you wanna play another round?(y/n):")












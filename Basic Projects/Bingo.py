#Global variables and imports

import random
min_num = 1
max_num = 10
guess_counts = 3

#Generating random number

def generate_random_num():
    return random.randint(min_num, max_num)
    


#Get Input


def get_guesses():
    print(f"The number you guess should be between {min_num}-{max_num} and You have {guess_counts} chances to guess right!")
    while True:
        try:
            guess_num = int(input("Enter your guess:"))
        except ValueError:
            print("Error : the number you entered is not Valid!")
        else:
            return guess_num



#Checking the guessed number

def check_guess_num(random_num,guess_num):
    return random_num == guess_num




#Runnig the application

def main():
    global guess_counts
    random_num = generate_random_num()
    print(random_num)
    while guess_counts > 0:
        guess_num = get_guesses()
        if check_guess_num(random_num, guess_num):
            print("You guessed right!")
            break
        guess_counts -= 1
        print(f"\nWrong number, You have {guess_counts} chances left! \n" )
    else:
        print("You lost!")
        
        
if __name__ == "__main__":
    main()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    


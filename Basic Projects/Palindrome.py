#imports and global variables


#getting inputs

def get_input():
    word = input("Enter your word: ")
    return word


#checking palindrome

def check_palindrome(word):
    return word == word[::-1]
        

#running main application

def main():
    word = get_input()
    if check_palindrome(word):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")



if __name__ == "__main__":
    main()

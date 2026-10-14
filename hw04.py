# ------------------------------------------------------
#        Name: Steph Krieger
#       Peers: (add any collaborators)
#  References: I looked at class slides and previous in class activities.
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """Checking user function for use of the secret word."""
    while True:
        text = input("Give me a sentence: ")
    
        if secret_word in text:
            print("You used the secret word!")
            break
    
        elif "dog" in text or "Dog" in text:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
    
        else:
            print("Try again")
        
    pass



# Task 2
def check_greater():
    """Comparing which integer the user inputs is greater."""
    while True:
        num1 = int(input("input an int:"))
        num2 = int(input("input an int:"))
        
        if num1 > num2:
            print("First is Greater")
            break
    
        elif num1 < num2:
            print("Second is Greater")
            break
    
        elif num1 == num2:
            print("Try again")
        
    pass



# Task 3
def get_special_numbers():
    """Listing the odd numbers that are also multiples of three and not multiples of five."""
    for i in range(40):
        even = i % 2 != 0
        mult3 = i % 3 == 0
        notmult5 = i % 5 !=0
        
        if even and mult3 and notmult5:
            print (i)
        
    pass


# Task 4.a
def my_for_loop():
    """Checks whether each letter in a word is a vowel or a consonant."""
    word = input("Enter a word: ")
    
    if len(word) < 2 or len(word) > 5 or " " in word:
        print("bad word")
        return
    
    for letter in word:
        if letter.lower() in "aeiou":
            print(letter, "is a vowel")
        else:
            print(letter, "is a consonant")
    pass

# Task 4.b
def my_while_loop():
    """Repeats a menu until the user chooses to stop."""
    while True:
        choice = input("Enter a, b, or c: ")

        if choice == "a":
            continue
        
        elif choice == "b":
            print("Goodbye")
            return
        
        elif choice == "c":
            exit()
            
        else:
            print("try again")
    pass

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

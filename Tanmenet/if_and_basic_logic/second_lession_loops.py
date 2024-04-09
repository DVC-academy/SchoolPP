"""
# Task00 - Counter:

-Get a number form the user.
-Use a while loop to print every natural number starting from 0 to the given number!
-Additional task (Task01B): check if the number is realy between 0 and 100
"""

def Task00():
    print("\n# Counter")
    num  = int(input("Enter a number: "))
    print(f"Counting Up from 0 to {num}:")
    i = 0
    while i <= num:
        print(i)
        i += 1

def Task00B():
    print("# Counter with check")
    num  = int(input("Enter a number between 0 and 100: "))
    if num < 0:
        print("Wrong number!")
    elif num > 100:
        print("Wrong number!")
    else:
        print(f"Counting Up from 0 to {num}:")
        i = 0
        while i <= num:
            print(i)
            i += 1

"""
# Task01 - Number Guessing Game:

-Pick a secret number between 1 and 10.
-Let the user guess the number in multiple attempts.
-Use if statements to check if the guess is too high, too low, or correct.
-Provide guidance and score feedback after each guess.
"""

def Task01():
    print("\n# Number Guessing Game")
    secret_number = 7
    attempts = 3

    while attempts > 0:
        guess = int(input("Guess the secret number (1-10): "))
        attempts -= 1

        if guess == secret_number:
            print("Congratulations, you guessed the number!")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

        if attempts == 0:
            print(f"Sorry, you ran out of guesses. The secret number was {secret_number}.")


# Comment out the functions here which you don't want to run!
Task00()
Task00B()
Task01()

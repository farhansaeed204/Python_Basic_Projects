from InquirerPy import inquirer
import random

playing = True

while playing:
    random_number = random.randint(1, 10)
    user_guess = int(input("Guess a number between 1 and 10: "))
    while user_guess != random_number:
        print("Opps you guess wrong number")
        user_guess = int(input("Guess a number between 1 and 10: "))
    
    print("Congratulations! You guessed the correct number.")

    choice = inquirer.select(
        message="Do you want to play again?",
        choices=["yes", "no"],
    ).execute()

    if choice == "no":
        playing = False
        print("Thanks for playing")
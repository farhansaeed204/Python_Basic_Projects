from InquirerPy import inquirer

print("Welcome to the Interactive Calculator!")


while True:
    user_input1 = int(input("Enter your first number: "))
    user_input2 = int(input("Enter your second number: "))
    choice = inquirer.select(
        message="Select a mathematical operation:",
        choices=["Addition", "Subtraction", "Multiplication", "Division"],
    ).execute()

    if choice == "Addition":
        result = user_input1 + user_input2
        print(f"The addition of {user_input1} and {user_input2} is: {result}\n")
    elif choice == "Subtraction":
        result = user_input1 - user_input2
        print(f"The subtraction of {user_input1} and {user_input2} is: {result}\n")
    elif choice == "Multiplication":
        result = user_input1 * user_input2
        print(f"The multiplication of {user_input1} and {user_input2} is: {result}\n")
    elif choice == "Division":
        result = user_input1 / user_input2
        print(f"The division of {user_input1} and {user_input2} is: {result}\n")
    
    choice2 = inquirer.select(
        message="Do you want to perform another calculation?",
        choices=["Yes", "No"],
    ).execute()

    if choice2 == "No":
        print("Thank you for using the Interactive Calculator. Goodbye!")
        break

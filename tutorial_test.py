def welcome():

    print(" ")
    print("Welcome to the CLI!")


def greet():

    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    print("Hello, " + first_name + " " + last_name + "!")


def guess_number():

    number = int(input(
        "please enter a number between 1 and 10 and i'll guess it: "))
    if number >= 1 and number <= 10:
        print("I guess your number is .... " + str(number) + "!")
    else:
        print("number out of range. Please try again.")
        guess_number()


def farewell():

    print("Thank you for participating in this CLI. Goodbye!")


while True:
    print("")
    print("choose an option!")
    print("1. welcome message")
    print("2. greeting message")
    print("3. guess number message")
    print("4. farewell message")

    choice = input("Please choose an option (1-4): ")

    if choice == "1":
        welcome()
    elif choice == "2":
        greet()
    elif choice == "3":
        guess_number()
    elif choice == "4":
        farewell()
        break
    else:
        print("Invalid choice. Please try again.")

def display_menu():
    print("1. Greet User")
    print("2. Even/Odd Checker")
    print("3. Exit")

def greet_user():
    print("Hello! Welcome to the program.")

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

def even_odd_checker_action():
    try:
        number = int(input("Enter an integer: "))
        check_even_odd(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def handle_menu_choice(choice):
    if choice == 1:
        greet_user()
        return False
    elif choice == 2:
        even_odd_checker_action()
        return False
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        return True
    else:
        print("Invalid choice. Please try again.")
        return False

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if handle_menu_choice(choice):
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
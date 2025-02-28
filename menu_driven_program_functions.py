def display_menu():
    print("Menu Options:")
    print("1. Display Greeting")
    print("2. Check Even or Odd")
    print("3. Exit")

def greet_user():
    print("Hello! Nice to see you.")

def even_odd_checker_action():
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def handle_menu_choice(choice):
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        return True
    else:
        print("Invalid choice! Please choose a valid option.")
        return False

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if handle_menu_choice(choice):
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
if __name__ == "__main__":
    main()
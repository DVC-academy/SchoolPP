import sys

theatre_name = sys.argv[1]
print(f"Welcome to the {theatre_name}!")
print("Please choose from the menu below:")

menu = ["1. List shows", "2. Buy ticket", "3. Refund a ticket", "4. Add new show", "5. Delete show", "6. Exit"]

exit_application = 1

while exit_application:
    for i in menu:
        print(i)

    option = input()
    match option:
        case "1":
            print("List shows:")
        case "2":
            print("Buy ticket:")
        case "3":
            print("Refund a ticket:")
        case "4":
            print("Add new show:")
        case "5":
            print("Delete show")
        case "6":
            print("Exiting the application...")
            exit_application = 0
        case _:
            print(f"{option} is not a valid menu point. Choose a valid option!")

print("Good bye!")
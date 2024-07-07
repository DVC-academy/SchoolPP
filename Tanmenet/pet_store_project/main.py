import sys

pet_store_name = sys.argv[1]
print(f"Welcome to the {pet_store_name}!")
print("Please choose from the menu below:")

menu = ["1. Available pets", "2. Add new pet", "3. Sell a pet", "4. Rename a pet", "5. Exit"]
pets = [
    ["Buksi", "dog", 3, "m"],
    ["Jágó", "parrot", 1, "m"]
]

exit_application = 1

while exit_application:
    for i in menu:
        print(i)

    option = input()
    match option:
        case "1":
            print("Available pets:")
        case "2":
            print("Add new pet:")
        case "3":
            print("Sell a pet:")
        case "4":
            print("Rename a pet:")
        case "5":
            print("Exiting the application...")
            exit_application = 0
        case _:
            print(f"{option} is not a valid menu point. Choose a valid option!")

print("Good bye!")


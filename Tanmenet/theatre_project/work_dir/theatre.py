import sys
import datetime


# theatre_name = sys.argv[1]
# print(f"Welcome to the {theatre_name}!")
print("  0 1 2 3 4 5 6 7 8 9 |")
occupied=[]
base_price = 5000
for letter in ["A", "B", "C"]:
    print(f"\033[0m{letter}", end=" ")
    for num in range(0, 10):
        if (letter + str(num)) in occupied:
            print(f"\033[91mX", end=" ")
        else:
            print(f"\033[0mO", end=" ")

    print(f"| {base_price} Ft")
    base_price-=500




print("Please choose from the menu below:")

menu = ["1. List shows", "2. Buy ticket", "3. Refund a ticket", "4. Add new show", "5. Delete show", "6. Exit"]
# id,title,available_tickets,price,stage,time
shows = [[0,"Diótörő", 20, 3000, "Tükörterem", "2025.01.01-19:00"],
         [1,"Székfoglaló", 20, 3000, "Tükörterem", "2025.01.02-19:00"],
         [2,"Káosz karnevál", 20, 5000, "Viharfelhő","2025.01.02-20:00"],
         [3,"Az igazság ára", 20, 100000, "Colosseum", "2025.01.02-17:00"]]



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
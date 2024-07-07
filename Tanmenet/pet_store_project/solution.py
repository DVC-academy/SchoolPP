import sys

pet_store_name = sys.argv[1]
print(f"Welcome to the {pet_store_name}!")

menu = ["1. Available pets", "2. Add new pet", "3. Sell a pet", "4. Rename a pet", "5. Exit"]
pets = [
    [1, "Buksi", "dog", 5000, 3, "m"],
    [2, "Jágó", "parrot", 4000, "m"]
]

run = 1

# Kiosztható feladatok


def add_new_pet():
    pet_id = int(input("Id of the pet:"))
    name = input("Name of the new pet:")
    species = input("Species of the new pet:")
    price = int(input("Price of the pet:"))
    age = int(input("Age of the new pet:"))
    sex = input("Sex of the new pet:")
    pets.append([pet_id, name, species, price, age, sex])
    print(f"New pet added: {name}, who is a {age} year(s) old {sex} {species}, and the its price is {price}")


#############################################################

# Main application

while run:
    print("Please choose from the menu below:")
    print("\n")
    for option in menu:
        print(option)

    option = input()
    match option:
        case "1":
            print("Available pets:")
            for pet in pets:
                print(f"id: {pet[0]}, name: {pet[1]}, species: {pet[2]}, price: {pet[3]}, age: {pet[4]}, sex: {pet[5]}")
        case "2":
            print("Add new pet:")
            add_new_pet()
        case "3":
            print("Sell a pet:")
        case "4":
            print("Rename a pet:")
        case "5":
            print("Exiting the application...")
            run = 0
        case _:
            print(f"{option} is not a valid menu point. Choose a valid option!")

print("Good bye!")


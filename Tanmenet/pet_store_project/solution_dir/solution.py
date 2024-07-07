import csv
import sys

pet_store_name = sys.argv[1]
print(f"Welcome to the {pet_store_name}!")

menu = ["1. Available pets", "2. Add new pet", "3. Sell a pet", "4. Rename a pet", "5. Exit"]
pets = [
    [1, "Buksi", "dog", 5000, 3, "m"],
    [2, "Jágó", "parrot", 4000, 4, "f"]
]

run = 1

# Kiosztható feladatok


def list_pets():
    for pet in pets:
        print(f"id: {pet[0]}, name: {pet[1]}, species: {pet[2]}, price: {pet[3]}Ft, age: {pet[4]}, sex: {pet[5]}")


def add_new_pet():
    pet_id = int(input("Id of the pet:"))
    name = input("Name of the new pet:")
    species = input("Species of the new pet:")
    price = int(input("Price of the pet:"))
    age = int(input("Age of the new pet:"))
    sex = input("Sex of the new pet:")
    pets.append([pet_id, name, species, price, age, sex])
    print(f"New pet added: {name}, who is a {age} year(s) old {sex} {species}, and the its price is {price}")


def handle_exit():
    print("Saving the pets...")
    with open('Tanmenet/pet_store_project/work_dir/save.csv', 'w') as file:
        writer = csv.writer(file)
        for row in pets:
            writer.writerow(row)
    print("Save complete!")
    print("Good bye!")

#############################################################

# Main application


while run:
    print("Please choose from the menu below:")
    for option in menu:
        print(option)

    option = input()
    match option:
        case "1":
            print("Available pets:")
            list_pets()
        case "2":
            print("Add new pet:")
            add_new_pet()
        case "3":
            print("Sell a pet:")
        case "4":
            print("Exiting the application...")
            run = 0
        case _:
            print(f"{option} is not a valid menu point. Choose a valid option!")
    print()

handle_exit()


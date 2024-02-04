
INDENT = "#######################################"

# 1. feladat: String használat
print("Így tudunk üzenetet kiírni.")

message = "Így pedig változón keresztül írhatunk ki valamit."
print(message)

# Konkatenáció
firstString = "Így lehet összekötni"
secondString = "két darab string-et."

print(firstString, secondString)


# 2. feladat: int-ek
print(2 + 3)

number = 2
number2 = 6
print(number + number2)

# Vegyes konkatenáció

print(firstString, 2, secondString)
print(firstString, number, secondString)

# Átláthatóság kedvéért: String interpoláció

stringToBeInserted = "szöveget"
numberToBeInserted = 5
print(f"Beírok ide valamennyi {stringToBeInserted} és egy számot is: {numberToBeInserted}.")

# Mi lenne ha ezt szeretnénk sokszor kiírni?
# Újra meg újra le kéne írni ezeket. Függvények bevezetése
# 3. feladat: függvények


def first_function():
    print("Ez egy üzenet a függvényen belül")
    message_in_function = "Ez egy változóba mentett üzenet a függvényen belül"
    print(message_in_function)
    print(2 + 3)

    number_in_function = 10
    number2_in_function = 12
    print(number_in_function + number2_in_function)


first_function()
first_function()
first_function()

# Mire jók még a függvények és miért is jók a változók?
# 4. feladat: paraméterek és visszatérési érték


def summary(first_number, second_number):
    return first_number + second_number


print(summary(10, 2))

# 4.b újra írni mindent amit eddig csináltunk fgv-ként, innentől mindent függvényként csinálunk.

def first_exercise():
    print("Ez egy üzenet a függvényen belül")
    message = "Ez egy változóba mentett üzenet a függvényen belül"
    print(message)
    print(2 + 3)

    number = 10
    number2 = 12
    print(number + number2)


print(INDENT)
first_exercise()
# second_exercise()
print(INDENT)





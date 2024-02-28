
INDENT = "#######################################"

# 1. feladat: String használat
print("Így tudunk üzenetet kiírni.")
message = "Így pedig változón keresztül írhatunk ki valamit."
print(message)


# Konkatenáció
string1 = "Így lehet összekötni"
string2 = "két darab string-et."
print(string1, string2)


# 2. feladat: int-ek
print(2 + 3)
number = 2
number2 = 6
print(number + number2)

# Vegyes konkatenáció
print(string1, 2, string2)
print(string1, number, string2)

# Átláthatóság kedvéért: String interpoláció

string_to_be_inserted = "szöveget"
number_to_be_inserted = 5
print(f"Beírok ide valamennyi {string_to_be_inserted} és egy számot is: {number_to_be_inserted}.")

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
# Először definiálom a függvényt -> nem történik semmi. Miért? -> meghívom a függvényt


def first_exercise():
    print("Első feladat:")
    print("Így tudunk üzenetet kiírni.")

    first_message = "Így pedig változón keresztül írhatunk ki valamit."
    print(first_message)

    # Konkatenáció
    first_string = "Így lehet összekötni"
    first_string2 = "két darab string-et."

    print(first_string + " " + first_string2)


def second_exercise():
    print("Második feladat:")
    print(2 + 3)

    second_number = 2
    second_number2 = 6
    print(second_number + second_number2)


print(INDENT)
first_exercise()
print(INDENT)
second_exercise()
print(INDENT)





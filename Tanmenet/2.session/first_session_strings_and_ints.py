
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
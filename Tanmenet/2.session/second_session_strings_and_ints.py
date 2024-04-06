#######################################################
INDENT = "#######################################"

print(INDENT)
print("1. feladat")
# 1. feladat: String használat
print("Így tudunk üzenetet kiírni.")
message = "Így pedig változón keresztül írhatunk ki valamit."
print(message)

# 1.1-es feladat (önálló)


# Konkatenáció
string1 = "Így lehet összekötni"
string2 = "két darab string-et."
string3 = "Meg esetleg egy harmadikat is."
print(string1, string2, string3)

# 1.2-es feladat (önálló)
start = "Szeretnék vásárolni"
amount1 = "egy"
amount2 = "kettő"
amount3 = "ezer"
name1 = "malacot."
name2 = "tehenet."
name3 = "tigrist."
print(start, amount3, name3)

#######################################################

print(f"\n{INDENT}")
print("2. feladat")
# 2. feladat: int-ek
print(2 + 3)
number = 2
number2 = 6
print(number + number2)

# 2.1-es feladat (önálló)
# 2.2-es feladat: változók felülírása (Mi lesz a konzol kimenetén?)
original = 12
print(original)
original = 15
print(original)


#######################################################


print(f"\n{INDENT}")
print("3. feladat")
# 3. Feladat: Vegyes konkatenáció, interpoláció
print(string1, 2, string2)
print(string1, number, string2)


string_to_be_inserted = "szöveget"
number_to_be_inserted = 5
print(f"Beírok ide valamennyi {string_to_be_inserted} és egy számot is: {number_to_be_inserted}.")

#######################################################

print(INDENT)
# 4. Feladat: Bekérés stdin-ről

#######################################################

# 5. Nagy feladat:

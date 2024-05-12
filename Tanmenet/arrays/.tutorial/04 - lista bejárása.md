# Lista bejárása

A listák a ciklusokkal együtt tudnak leginkább kiteljesedni. Egy listán végig tudunk menni például `for loop` segítségével:

```python
students = ["Peti", "Kata", "Legolasz", "Béla"]

for student in students:
    print(student)
```

Lehet persze indexeket is használni ha példul csak a lista egy részén akarunk végig menni:

```python
students = ["Peti", "Kata", "Legolasz", "Béla"]

for i in [0,1,3]:
    print(students[i])
```
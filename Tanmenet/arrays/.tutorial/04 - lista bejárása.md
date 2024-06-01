# Lista bejárása

A listák a ciklusokkal együtt tudnak leginkább kiteljesedni. Egy listán végig tudunk menni például `for loop` segítségével:

```python
students = ["Peti", "Kata", "Legolasz", "Béla"]

for student in students:
    print(student)
```

Lehetséges a `range()` függvény segítségével is végig menni:

```python
students = ["Peti", "Kata", "Legolasz", "Béla"]

for i in range(len(students)):
    print(students[i])
```

Konkrét ndexeket is használhatunk, ha csak a lista egy részén akarunk végig menni:

```python
students = ["Peti", "Kata", "Legolasz", "Béla"]

for i in [0,1,3]:
    print(students[i])
```
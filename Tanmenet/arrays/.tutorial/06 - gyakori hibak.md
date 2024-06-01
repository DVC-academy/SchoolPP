# Gyakori hibák

## Nem létező indexekre hivatkozás

A programunk hibát fog dobni ha egy olyan elemre hivatkozunk ami nem létezik!

Például:
```python
my_list = ["traktor", True, 42, "másik traktor"]  
print(my_list[10]) 
```

Ugynanúgy ügyelni kell erre tartomány esetén is!

Például:
```python
my_list = ["traktor", True, 42, "másik traktor"]  
print(my_list[2:8]) 
```

## Javítsd ki a kódot!

Egy listában a szivárvány színeit tároljuk majd kiírjuk őket. Javítsd ki az alábbi kódot!

```python
rainbow = ["red", "orange", "yellow", "green", blue, "violet")

for colors in rainbow
print(color)
  
```


Egy listában az osztály tanlói vannak felsorolva és ki akarjuk őket írni egymás alá. Javítsd ki az alábbi kódot!

```python
students = ["Peti", "Kata", "Legolasz", "Béla"]

for i in range(students):
    print(students[i])
```

#TODO: még példák
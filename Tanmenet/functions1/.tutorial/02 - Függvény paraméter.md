# Függvények paraméterekkel

```python
def print_name(name):
    print(f"My name is {name}")
```

- A függvény bemenő paramétereit a függvény neve után zárójelben adjuk meg. Ebben az esetben a `name` a bemenő paraméter neve.

## Mire jók a paraméterek?

- A paraméterek segítségével tudunk adatokat átadni a függvénynek, amelyekkel dolgozni tud.
- Megváltoztathatjuk a függvény működését anélkül, hogy a függvényt módosítanánk.

## Példa

```python
def print_name(name):
    print(f"My name is {name}")

print_name("John")
print_name("Jane")
```

Ha lefuttatjuk a kódot, láthatjuk, hogy az egyik esetben a `name` értéke `John`, a másik esetben pedig `Jane`. </br>
Ugyanazt a függvényt használtuk, amin belül ugyanaz történt, mégis két különböző eredményt kaptunk.

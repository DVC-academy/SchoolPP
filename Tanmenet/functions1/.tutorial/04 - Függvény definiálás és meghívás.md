# Függvény definició és meghívás

TODO: lehet több paraméter is 

```python
def print_my_name():
    print("My name is Vince")

def print_color(color):
    print(f"My kedvenc color is {color}")

def add(a, b):
    return a + b

```

- Ha bemásoljuk a függvény kódját és lefuttatjuk a scriptet, azt fogjuk tapasztalni, hogy semmi sem történik.
- Azzal, hogy egy függvényt definiálunk (`def`), még nem hívjuk meg azt. A függvényeket külön kell meghívni, hogy a kódjuk lefusson.
- A függvényt a nevével és zárójelben megadott paraméterekkel hívjuk meg.

```python
print_my_name()
print_color("Babakék")
print(add(2, 3))
```

## Függvény visszatérési értékének használata
Az előző példában azt láttuk, hogy az `add` függvény meghívásra kerül egy `print` függvény paramétereként.
Ez azt jelenti, hogy amit az `add` függvény visszaad, azt a `print` függvény azonnal kiírja a képernyőre.
Azonban a függvények visszatérési értékét változóként is eltárolhatjuk.

```python
def add(a, b):
    return a + b
    
result = add(2, 3)
print(result)
```
Ebben a példában először definiálunk egy `add` függvényt, amely visszaadja az `a` és `b` paraméterek összegét.
Ezután a `result` változóban eltároljuk az `add` függvény visszatérési értékét.
Végül a `result` változót kiírjuk a képernyőre.
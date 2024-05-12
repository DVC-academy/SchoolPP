# Scope

## Mit jelent a scope?

Ezt egy egyszerű példán keresztül fogjuk megérteni.

```python
def my_function():
    x = 10
    print(x)

my_function()
print(x)
```
Azt láthatjuk, hogy a `x` változó a `my_function` függvényen belül van definiálva. </br>
Ez azt jelenti, hogy amikor az utolsó sorban ki akarjuk írni a `x` változót, akkor hibát fogunk kapni, mert a `x` változó csak a `my_function` függvényen belül érhető el.
Ezt nevezzük a változó scope-jának. Ez a változó csak a függvényen belül érhető el.


## Globális és lokális scope

A változók lehetnek globálisak és lokálisak. </br>
A globális változók azok, amelyek a fájl tetején vannak definiálva, és az egész fájlban elérhetőek. </br>
A lokális változók azok, amelyek csak a függvényen belül érhetőek el.

Nézzük meg ezt az elsőre kicsit zavarosnak tűnő példát:
```python
x = 10

def my_function():
    x = 20
    print(x)

my_function()
print(x)
```

A fenti példában a `x` változó két helyen is definiálva van. Az első definiálás a fájl tetején történik, tehát ez egy globális változó. A második definiálás a `my_function` függvényen belül történik, tehát ez egy lokális változó. </br>
Próbáld meg a kód lefuttatása nélül megmondani, hogy mi lesz a kimenet.


<details><summary> Válasz </summary>

A kimenet a következő lesz:

```python
20
10
```
### De miért? </br>
Amikor a `my_function` függvényt meghívjuk, akkor a `x` változó értéke 20 lesz a függvényen belül, és ezt fogjuk kiírni a képernyőre. </br>
Amikor a `my_function` függvény lefutott, akkor folytatódik a program futása, és a `print(x)` sorban a globális `x` változót fogjuk kiírni a képernyőre.


</details>
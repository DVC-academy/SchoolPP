# Kiíratás, bekérés

## Kiíratás a konzolra

Ha szeretnénk megnézni egy változó aktuális értékét, akkor ki tudjuk írni a konzolra.
Példa:

```python
name = "Alex"
print(name)
```

Ebben a példában azt láthatjuk, ahogy az első sorban a **name** nevű változónak átadjuk az **Alex** értéket, a második sorban pedig kiíratjuk a **name** nevű változó értékét, így a konzolon kiírva azt fogjuk látni hogy:
Alex

Ugyanez int-ek esetében így néz ki:
```python
number = 12
print(number)
```

## Bekérés a konzolról
Ugyanígy, ahogy a program futása közben ki tudunk nyerni információt a változók aktuális állapotáról, be is tudunk juttatni adatot.
Ennek a módját az alábbiakban láthatod:

```python
name = input()
print("Szia", name)
```

Ez a rövid program bekér a konzolról egy szöveget, majd elmenti azt a name nevű változóban.
Az `input()` egy úgy nevezett függvény, ami azért felel, hogy a konzolra beírt szöveget behozza a programba.

### Bekérés a konzolról üzenettel
Az `input()` függvényt megkérhetjük arra is, hogy írjon ki egy üzenetet a konzolra, hogy a felhasználó tudja mi a feladata. Pl:

```python
name = input("Írd be a neved:")
print("Szia", name)
```
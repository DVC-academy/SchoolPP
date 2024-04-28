# Gyakori hibáka while loop használatánál

## Végtelen ciklus

`Futtasd` ezt a kódot. Mi történik?

```python
szamlalo = 0
while szamlalo < 10:
  print(szamlalo)
```

<details> <summary>  Válasz </summary>
  
A futtatás során a végtelenségig 0-ákat látsz nyomtatódni. Miért?  Végtelen ciklust hoztál létre, mert ebben az esetben a számláló mindig kisebb lesz 10-nél. Állítsd le manuálisan a programot, és add meg a `szamlalo += 1` utasítást.

```python
szamlalo = 0
while szamlalo < 10:
  print(szamlalo)
  szamlalo += 1
```
</details>

## Semmi sem történik...

`Futtasd` ezt a kódot. Mi a hiba?

```python
szamlalo = 0
while szamlalo > 6:
  print(szamlalo)
  szamlalo += 1 
```

<details> <summary>  Válasz </summary>
  
A probléma a feltétel. Fordítva van megadva. Az egyenlőtlenség azt mondja, hogy ha a számláló nagyobb, mint 6, akkor adjunk hozzá egyet. A számláló azonban 0. Ezért kiindulásilag nem nagyobb, mint hat.

Javítsd ki az egyenlőtlenséget `<`-re.

</details>

## Kilépés

Szöveggel is használhatsz `while` ciklust. Az alábbi kódban a while feltétel azt mondja: "amíg nem írsz be igent, a számítógép azt írja ki 'Futok'"

`Futtasd` ezt a kódot. Mit látsz?

```python
kilepes = ""
while kilepes != "igen":
  print("Futok")
kilepes = input("Kilépés?: ")
```

<details> <summary>  Válasz </summary>

Ellenőrizd a behúzásodat. A feltételt szabályozó változót a ciklus *belül* kell módosítani.

```python
kilepes = ""
while kilepes != "igen":
  print("Futok")
  kilepes = input("Kilépés?: ")
```
</details>

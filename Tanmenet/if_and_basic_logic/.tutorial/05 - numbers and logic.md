# Relációs jelek

A Pythonban a következő relációs jeleket lehet használni:

* **Egyenlőség (`==`):** Két érték egyenlőségének ellenőrzésére szolgál. Például: `5 == 5` igaz, `3 == 2` hamis.
* **Különbség (`!=`):** Két érték különbözőségének ellenőrzésére szolgál. Például: `5 != 5` hamis, `3 != 2` igaz.
* **Kisebb (`<`):** Annak ellenőrzésére szolgál, hogy az egyik érték kisebb-e, mint a másik. Például: `3 < 5` igaz, `5 < 3` hamis.
* **Nagyobb (`>`):** Annak ellenőrzésére szolgál, hogy az egyik érték nagyobb-e, mint a másik. Például: `5 > 3` igaz, `3 > 5` hamis.
* **Kisebb vagy egyenlő (`<=`):** Annak ellenőrzésére szolgál, hogy az egyik érték kisebb-e vagy egyenlő a másikkal. Például: `5 <= 5` igaz, `3 <= 5` igaz, `5 <= 3` hamis.
* **Nagyobb vagy egyenlő (`>=`):** Annak ellenőrzésére szolgál, hogy az egyik érték nagyobb-e vagy egyenlő a másikkal. Például: `5 >= 5` igaz, `5 >= 3` igaz, `3 >= 5` hamis.

A relációs jelek számok, szövegek és booleán értékek összehasonlítására használhatók. Például megadhatunk egy feltételt a segítségükkel egy `if` utasításban.

Példa a szintaxishoz:

```python
if A > B:
    print("A nagyobb mint B!")
else:
    print("A nem nagyobb mint B!")
```



### Korhatár

- Kérd be a felhasználó életkorát.
- Használj `if` utasítást annak eldöntésére, hogy jogosult-e szavazni.
- Nyomtasson ki informatív üzeneteket a kora alapján.

<details><summary> Lehetséges megoldás </summary>
  
```python
print("\n# Korhatár")
szavazati_korhatar = 18
kor = int(input("Add meg a korod: "))

if kor >= szavazati_korhatar:
  print("Jogosult vagy szavazni!")
else:
  szavazasig_hatra = szavazati_korhatar - kor
  print(f"Még nem jogosult szavazni. {szavazasig_hatra} év múlva szavazhatsz.")
```
</details>

### Hőmérséklet-ellenőrző:

- Kérd be a felhasználótól az aktuális hőmérsékletet.
- Használj `if` utasításokat a hőmérséklet "hideg", "meleg" kategóriába sorolásához a megfelelő küszöbértékek alapján.
- Írass ki megfelelő üzeneteket a hőmérsékleti kategória alapján.

<details><summary> Lehetséges megoldás </summary>
  
```python
print("\n# Hőmérséklet-ellenőrző")
homerseklet = float(input("Add meg az aktuális hőmérsékletet (°C-ban): "))

if homerklet <= 20:
  kategoria = "hideg"
else:
  kategoria = "meleg"

print(f"Az aktuális hőmérséklet {homerseklet}°C, ami egyesek szerint {kategoria}")
```
</details>

- Adj hozzá további hőmérsékleteket is!

<details><summary> Lehetséges megoldás </summary>

```python
print("\n# Hőmérséklet-ellenőrző")
homerseklet = float(input("Add meg az aktuális hőmérsékletet (°C-ban): "))

if homerklet <= 20:
  kategoria = "hideg"
elif homerklet <= 25:
  kategoria = "langyos"
else:
  kategoria = "meleg"

print(f"Az aktuális hőmérséklet {homerseklet}°C, ami egyesek szerint {kategoria}")
```
</details>


### Osztályzat-átváltó:

- Kérj be a felhasználótól a számszerű osztályzatát.
- Használj `if` utasításokat a betűs osztályzatok hozzárendelésére egy osztályozási skála alapján (szükség szerint igazítsd a tartományokat).
- Írd ki a megfelelő betűs osztályzatot.

<details><summary> Lehetséges megoldás </summary>

```python
print("\n# Osztályzat-átváltó")
osztalyzat = int(input("Add meg a számszerű osztályzatod (0-100): "))

if osztalyzat >= 90:
  betűs_osztalyzat = "A"
elif osztalyzat >= 80:
  betűs_osztalyzat = "B"
elif osztalyzat >= 70:
  betűs_osztalyzat = "C"
elif osztalyzat >= 60:
  betűs_osztalyzat = "D"
else:
  betűs_osztalyzat = "F"

print(f"A betűs osztályzatod: {betűs_osztalyzat}")
```
</details>



### Szám összehasonlítás:

- Kérd meg a felhasználót, hogy adjon meg két számot.
- Használj `if` utasítást annak ellenőrzésére, hogy az első szám nagyobb, kisebb vagy egyenlő-e a második számmal.
- Írd ki a megfelelő üzeneteket az összehasonlítás alapján.


<details><summary> Lehetséges megoldás </summary>

```python
print("\n# Szám összehasonlítás")
szam1 = int(input("Add meg az első számot: "))
szam2 = int(input("Add meg a második számot: "))

if szam1 > szam2:
  print(f"{szam1} nagyobb, mint {szam2}.")
elif szam1 < szam2:
  print(f"{szam1} kisebb, mint {szam2}.")
else:
  print(f"{szam1} egyenlő {szam2}-vel.")
```
</details>
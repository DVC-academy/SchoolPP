# Gyakori hibák a for loop és range használatánál

## Érvénytelen szintaxis

**Mi a probléma ezzel a programmal?**

A programnak össze kellene adnia a 0-tól 99-ig terjedő számokat, és folyamatosan ki kellene írnia az összeget. Miért nem működik?

```python
total = 0
for number in range 100: 
  total += number
  print(total)
```
<details> <summary> Válasz </summary>

Elfelejtettük a zárójeleket a `range` függvénynél. A zárójelek fontosak, mert a `range` egy függvény (mint a `exit` függvény). A `range` feladata, hogy számokat tartalmazó listát hozzon létre 0 és a zárójelbe tett szám között. Ha nincsenek zárójelek, akkor nem fog működni.

**Helyes kód:**

```python
total = 0
for number in range(100):  # Helyes zárójelekkel
  total += number
  print(total)
```
</details>

## Névhiba

**Mi a probléma ezzel a programmal?**

Ebben a programban a számítógépnek ki kellene írnia a "n. Nap" szöveget az 1-6-os számokkal együtt. Miért írja azt, hogy "nap nincs definiálva"?

```python
for days in range(7):
  print(f"{day}. Nap") 
```

<details> <summary> Válasz </summary>

A változó neve hibás a kódban. Ha egy létrehozott változóra szeretnél hivatkozni egy `for` ciklusban, akkor minden alkalommal ugyanúgy kell írni.

**Helyes kód:**

```python
for days in range(7):
  print(f"{days}. Nap")  # Helyes változó név használata
```
</details>

## Tartomány hiba

```python
for i in range (10, 0):
    print(i)
```
<details> <summary> Válasz </summary>

**A lépésköz hiányzik a range() függvényben**

A `for i in range (10, 0)` kód futtatási hibát okoz. A `range()` függvény három argumentumot fogadhat el: a kezdőértéket, a végértéket és a lépésközt. A te esetedben hiányzik a harmadik argumentum, a lépésköz.

* Alapértelmezés szerint a `range()` függvény 1-es lépésközt használ. Ez azt jelenti, hogy a hibaüzenet arra utal, hogy a kódod valójában a következőt mondja a számítógépnek: "kezdj 10-nél, folytasd 0-ig, és minden alkalommal növeld 1-gyel". Ez nem kivitelezhető, mert 10-et nem lehet elérni 0-tól indulva 1-es lépésekkel történő növeléssel. Emiatt a kód nem fog futni.

* A probléma megoldásához explicit módon meg kell adnod a lépésközt a `range()` függvény harmadik argumentumaként. A visszafelé számláláshoz -1-es lépésközt kell használni. Így a helyes kód a következő:

```python
for i in range(10, 0, -1):
    print(i)
```

</details>

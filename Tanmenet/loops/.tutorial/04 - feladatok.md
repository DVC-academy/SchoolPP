# Feladatok

## Számláló:

1. Kérjünk egy számot a felhasználótól.
2. Ellenőrizzük, hogy a szám valóban 0 és 100 között van-e! 
3. Használjunk egy `while` ciklust minden természetes szám kiírására 0-tól a megadott számig!

<details> <summary>  Lehetséges megoldás </summary>

```python
szam = int(input("Írj be egy számot 0 és 100 között: "))
if szam < 0:
  print("Helytelen szám!")
elif szam > 100:
  print("Helytelen szám!")
else:
  print(f"0-tól {szam}-ig számolok:")
  i = 0
  while i <= szam:
    print(i)
    i += 1
```
</details>

## Páros vagy Páratlan számláló

1. Módosítsuk az előző feladatok hogy egy plusz kérdést is felteszünk: Hányasával akar elszámolni a megadott számig?
2. Ellenőrizd le hogya második szám is 1 és 100 között van-e!

<details> <summary>  Lehetséges megoldás </summary>

```python
szam = int(input("Írj be egy számot 0 és 100 között: "))
if szam < 0 or szam > 100:
  print("Helytelen szám!")
else:
  novel = int(input("Írj be egy számot 0 és 100 között amivel növekedni fog a számlálás: "))
  if szam < 0 or szam > 100::
    print("Helytelen szám!")
  else:
    print(f"0-tól {szam}-ig számolok {novel} hosszú közökkel:")
    i = 0
    while i <= szam:
      print(i)
      i += novel
```
</details>

## Szám Tippelő Játék:

1. Válassz egy titkos számot 1 és 10 között.
2. Add meg a felhasználónak a lehetőséget, hogy kitalálja a számot több próbálkozással.
3. Használj `if` utasításokat annak ellenőrzésére, hogy a tipp túl magas, túl alacsony vagy éppen sikerült eltalálni.


<details> <summary>  Lehetséges megoldás </summary>

```python
titkos_szam = 7
probalkozasok = 3

while probalkozasok > 0:
  tipp = int(input("Találd ki a titkos számot (1-10): "))
  probalkozasok -= 1  # Csökkenti a hátralévő próbálkozások számát 1-gyel

  if tipp == titkos_szam:
    print("Gratulálunk, kitaláltad a számot!")
    break  # Kilép a ciklusból, ha a szám kitalálásra került

  elif tipp < titkos_szam:
    print("Túl alacsony. Próbáld újra!")

  else:
    print("Túl magas. Próbáld újra!")

if probalkozasok == 0:
  print(f"Sajnálom, elfogytak a próbálkozásaid. A titkos szám {titkos_szam} volt.")
```
</details>

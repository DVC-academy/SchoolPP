# Gyakorló feladatok

### Számtippelés

- Írj egy programot ami 'if'-ek segítségével és egymás utáni eldöntendő kérdéssel kitalálja hogy melyik számra gondolt a felhasználó 1 és 5 között! Lehetőleg minél kevesebb kérdéssel!
- A válaszok lehetnek i/I ami igent, vagy n/N ami a nemet jelenti!
- 
<details><summary> Lehetséges megoldás </summary>
  
```python
print("\n# Gondolj egy számra 1 és 5 között!")

hatar34 = input("A gondolt szám nagyobb mint három? (i/n) ")
if hatar34 == "i" or hatar34 == "I":
  hatar45 = input("A gondolt szám nagyobb mint négy? (i/n) ")
  if hatar45 == "i" or hatar45 == "I":
    print("Ezek alapján a gondolt szám: 5")
  else:
    print("Ezek alapján a gondolt szám: 4")
else:
  hatar23 = input("A gondolt szám nagyobb mint kettő? (i/n) ")
  if hatar23 == "i" or hatar23 == "I":
    print("Ezek alapján a gondolt szám: 3")
  else:
    hatar12 = input("A gondolt szám nagyobb mint egy? (i/n) ")
    if hatar12 == "i" or hatar12 == "I":
      print("Ezek alapján a gondolt szám: 2")
    else:
      print("Ezek alapján a gondolt szám: 1")
```
</details>


### E-mail 
Kérj inputról két nevet egymás után: egy feladót és egy címzettet. 
Írj egy egyszerű üdvözlő levelet melynek melbyen a megszólításnál és elköszönésnél felhasználod ezeket a neveket.
pl: Kedves {címzett}, nagyon szép napunk van ma! Remélem te is a megfelelő pártra szavazol! Üdvözlettel: {feladó}

### Szidalmazás generátor 
Kérj inputról két szót egymás után: egy melléknevet és egy főnevet.
Ír egy egyszerű szidalmazást ezek segítségével!
pl: A {melléknév} édesanyád is ezt mondta amikor előkerült tegnap az ágyban egy {főnév} és akkor nem panaszkodott.

### Számológép
Írj egy egyszű számológépet!

### Téglalap területszámítása
Kérj bementről két számot egymás után: a téglalap maagasságát és szélességét.
Írd ki a téglalap kerületét és területét!
(ugyanez más matematikai alakzatokkal lehet remixelve)

### Pythonagorasz 
Kérj bementről két számot egymás után: egy derékszögű háromszög két befogójának hosszát cm-ben.
Írd ki a derékszögű háromszög átfogóját miliméterben!
(Más tulajodnásgit is ki lehet íratni)

### Időszámítás
Kérj bementről egy egész számot (0-86 400)! 
Írd ki hogy mi lenne a pontos idő, ha a bemenetül kapot számnyi másodperc telt volna el éjfél óta!
pl: bemenet=3666 kimenet=01:01:06 
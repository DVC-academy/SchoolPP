# Gyakorló feladatok

### Számtippelés

- Írj egy programot ami 'if'-ek segítségével és egymás utáni eldöntendő kérdéssel kitalálja hogy melyik számra gondolt a felhasználó 1 és 5 között! Lehetőleg minél kevesebb kérdéssel!
- A válaszok lehetnek i/I ami igent, vagy n/N ami a nemet jelenti!
  
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


### Számológép
Írj egy egyszű számológépet! Tudja kezelni a 4 alapműveletet (összeadás, kivonás, szorzás, osztás)!


### Kő-papír-Olló

1. A játék két játékossal működik: 1. játékos és 2. játékos.
2. A program logikájához if (ha) feltételekre lesz szükség, lehet, hogy egymásba ágyazva, hogy eldöntsd ki nyert, kikapott, vagy döntetlen lett a játék.
3. Fűszerezd meg a játékot! Használj vicces kommenteket, hogy izgalmasabb legyen a küzdelem.
4. Egyszerűsítsd le a dolgot magadnak! Ne várd el a játékostól, hogy kiírja a teljes szót (kő, papír, olló). helyette hasznosítsd az egyszerű rövidítéseket: K (kő), P (papír), O (olló). Kezeld a hibás bevitelt! 


<details> <summary>  Lehetséges megoldás  </summary>

```python

print("E P I C    🪨 📄 ✂️    B A T T L E ")
print()
print("Válassz fegyvert! (k, p vagy o)") 
print()

jatekos1_lepes = input("1. játékos > ")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
jatekos2_lepes = input("2. játékos > ")
print()

if jatekos1_lepes == "k":
    if jatekos2_lepes == "k":
        print("Mindketten követ választottatok, döntetlen!")  
    elif jatekos2_lepes == "o":
        print("Az 1. játékos kővé porlasztotta a 2. játékos ollóját!")  
    elif jatekos2_lepes == "p":
        print("Az 1. játékos kövét eltemeti a 2. játékos papírja!") 
    else:
        print("Érvénytelen 2. játékos!")  
elif jatekos1_lepes == "p":
    if jatekos2_lepes == "k":
        print("A 2. játékos kövét eltemeti az 1. játékos papírja!") 
    elif jatekos2_lepes == "o":
        print("Az 1. játékos papírját apró darabokra vágja a 2. játékos ollója!")  
    elif jatekos2_lepes == "p":
        print("Két papírlap csap össze egymással. Kiábrándító. Döntetlen.") 
    else:
        print("Érvénytelen fegyver 2. játékos!")  
elif jatekos1_lepes == "o":
    if jatekos2_lepes == "k":
        print("A 2. játékos köve fémport kavar az 1. játékos ollójából!") 
    elif jatekos2_lepes == "o":
        print("Kaszálás! Az ollók egymáshoz csattannak, mint egy silány kardvívás! Döntetlen.") 
    elif jatekos2_lepes == "p":
        print("Az 1. játékos ollója konfettire vágja a 2. játékos papírját!")  
    else:
        print("Érvénytelen fegyver 2. játékos!")  
else:
    print("Érvénytelen fegyver 1. játékos!") 


```

</details>
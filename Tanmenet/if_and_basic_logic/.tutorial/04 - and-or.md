# And és or utasítás

Az `and` és `or` utasítás logikai műveletek, melyek arra szolgálnak hogy egyszerre több logikai állítást tudjunk megvizsgálni.

* Az **A** és **B** két logikai állítást jelöl, amelyek lehetnek igazak vagy hamisak.
* Az `or` művelet eredménye igaz, ha **A _vagy_ B**, vagy mindkettő igaz, egyébként hamis.
* Az `and` művelet eredménye csak akkor igaz, ha **A _és_ B** egyszerre igaz, egyébként hamis.

Íme egy táblázat ami segít összefoglalni őket:

| A | B | &rarr; | **A `or` B**  | **A `and` B** |
|:---:|:---:|:---:|:---:|:---:|
| _Igaz_ | _Igaz_ | &rarr; | **Igaz** | **Igaz** |
| _Igaz_ | _Hamis_ | &rarr; | **Igaz** | **Hamis** |
| _Hamis_ | _Igaz_ | &rarr; | **Igaz** | **Hamis** |
| _Hamis_ | _Hamis_ | &rarr; | **Hamis** | **Hamis** |

Példa az `or` műveletre:
```python
if A or B:
  print("A vagy B állítás igaz!")
else:
  print("A és B állítás hamis!")
```

Példa az `and` műveletre:
```python
if A and B:
  print("A és B állítás igaz!")
else:
  print("A vagy B állítás hamis!")
```

&nbsp;

---

### Gyakorlás

Módosítsuk az előző feladatot az `or` művelet használatával!
A program üdvözöljön ha a megadott név az "Dávid" vagy "Vince" vagy a te neved, egyébként pedig mondd meg a felhasználónak hogy itt nem tud belépni!
Ne használj `elif` utasítást a programban!

<details><summary> Lehetséges megoldás </summary>
  
```python
myName = input("Mi a neved?: ")
if myName == "Dávid" or myName == "Vince":
  print(f"Szia {myName}, már vártalak!")
else:
  print("Tűnj el!")
```
</details>

### Felhasználónév és jelszó

Kérjünk be további bemenetként egy jelszót is!
1. Először csak a felhasználó nevet kérje be a progam és azt ellenőrizze ahogy korábban is! 
2. Ha a felhasználónév el lett fogadva kérjünk be jelszót is és ellenőrizzük hogy az stimmel-e a felhazsnálónévez megadottal!
3. Dávid jelszava legyen "password", Vince jelszava pedig "safePassword123"!

<details><summary> Lehetséges megoldás </summary>
  
```python
print("BIZTONSÁGOS BEJELENTKEZÉS")
userName = input("Felhasználónév > ")

if userName == "Dávid" or userName == "Vince":
  print(f"Szia {userName}, már vártalak!")
  password = input("Jelszó > ")
  if (userName == "Dávid" and password == "password") or (userName == "Vince" and password == "safePassword123"):
    print("Helyes a jelszó, tényleg te vagy az!")
  else:
    print("Helytelen a jelszó! Úgy tűnik átvertél :/")
else:
  print("Tűnj el!")
```
</details>




# And és or utasítás

TODO: kifejteni az and-et és az or-t

Az **or** kulcsszóval le tudjuk egyszerűsíteni az előzőt:

```python
myName = input("Mi a neved?: ")
if myName == "Dávid" or myName == "Vince":
  print(f"Szia {myName}, már vártalak!")
else:
  print("Tűnj el!")
```

 ### Adjunk hozzá még egy kis bemenetet.

Módosítsuk a kódot, hogy mind a névnek **és** a jelszónak egyeznie kell ahhoz, hogy Dávid és Vince be tudjanak jelentkezni.


```python
print("BIZTONSÁGOS BEJELENTKEZÉS")
username = input("Felhasználónév > ")
password = input("Jelszó > ")
```

&nbsp;

Az alábbi kódban a felhasználónévnek és a jelszónak **egyaránt** helyesnek kell lennie ahhoz, hogy Márk be tudjon jelentkezni.

TODO: case-ek egységesítése

```python
print("BIZTONSÁGOS BEJELENTKEZÉS")
username = input("Felhasználónév > ")
password = input("Jelszó > ")

if username == "Dávid" and password == "password":
  print("Szia Dávid, már vártalak!")
else:
  print("Tűnj el!")
```

&nbsp;

Vince jelszava a "safePassword123". Add hozzá ezt a kódhoz

<details><summary> Válasz </summary>

```python
print("BIZTONSÁGOS BEJELENTKEZÉS")
username = input("Felhasználónév > ")
password = input("Jelszó > ")

if username == "Dávid" and password == "password":
  print("Szia Dávid, már vártalak!")
elif username == "Vince" and password == "safePassword123":
  print("Szia Vince, már vártalak!")
else:
  print("Tűnj el!")
```
</details>

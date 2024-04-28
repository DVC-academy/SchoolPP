# If utasítás

Ezek az utasítások egy kicsit olyanok, mintha kérdést tennénk fel. 

Azt mondjuk a számítógépnek: ha (`if`) valami igaz, akkor (`then`) hajtsa végre ezt a specifikus kód blokkot.

A dupla egyenlőség (`==`) arra kéri a számítógépet, hogy hasonlítsa össze, vajon ez a két dolog **pontosan** egyforma-e.

&nbsp;

Ahhoz, hogy az `if` utasítás bemenetéhez kapcsolódó `print` utasítást hozzunk létre, a következő sorba kell lépnünk, és **egyszer** kell behúznunk (tabulátor) a kódot (szerencsére a Replit megteszi, de légy óvatos!). 

 Másold át ezt a kódot, és nézd meg, mi történik!
  
```python
myName = input("Mi a neved?: ")
if myName == "Dávid":
  print("Szia Dávid, már vártalak!")
```
  
## Else utasítás

Ha a feltétel **nem** teljesül az `if` utasításban, akkor azt szeretnénk, hogy a számítógép az `else` részt hajtsa végre helyette.

Hasonlóképpen, ha a feltétel **teljesül** az `if` utasításban, akkor az `else` részt a számítógép figyelmen kívül hagyja.

Az `else` utasításnak az `if` utasítás után az első **behúzatlan** sort kell elfoglalnia, és egy vonalban kell lennie azzal (a Replit itt is segít).

Másold át ezt a kódot, és nézd meg, mi történik!

```python
myName = input("Mi a neved?: ")
if myName == "Dávid":
  print("Szia Dávid, már vártalak!")
else:
  print("Ki a fene vagy te?!")
```



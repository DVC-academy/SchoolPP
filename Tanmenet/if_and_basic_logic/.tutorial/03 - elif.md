# Elif utasítás

Az `elif` parancs (ami az 'elseif' rövidítése) lehetővé teszi, hogy 2, 3, 4 vagy akár 99999999994 kérdést is feltegyünk ugyanazzal a bemenettel! Ez a parancs egy meghatározott helyen kell tartózkodjon. Annyi `elif` utasításod lehet, amennyit csak akarsz, de **kötelezően** az `if` és `else` közé kell helyezniük, és ugyanazzal a behúzással kell rendelkezniük.

Az `elif` parancsban található `print` utasításoknak a többi `print` utasítás behúzásával kell egyezniük.

&nbsp;

Nézzük meg egy korábbi példába hogyan illeszthető be egy elif!

```python
myName = input("Mi a neved?: ")
if myName == "Dávid":
  print("Szia Dávid, már vártalak!")
elif myName == "Vince":
  print("Szia Vince, már nagyon vártalak!")
else:
  print("Ki a fene vagy te?!")
```

### Feladat
Próbáld meg hozzáadni a saját neved is, hogy téged is üdvözöljön!

<details><summary> Megoldás </summary>
  
```python
myName = input("Mi a neved?: ")
if myName == "Dávid":
  print("Szia Dávid, már vártalak!")
elif myName == "Vince":
  print("Szia Vince, már nagyon vártalak!")
elif myName == "Név":
  print("Szia Név, csak rád vártam!")
else:
  print("Ki a fene vagy te?!")
```
</details>
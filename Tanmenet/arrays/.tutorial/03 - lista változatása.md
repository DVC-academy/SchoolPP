## Elemek módosítása és beszúrása listában

**Elem érték módosítása**

A lista egy adott elemének értékét az indexszám alapján módosíthatjuk:

A második elem módosítása:

```python
gyumolcsok = ["alma", "banán", "traktor"]
gyumolcsok[2] = "fekete ribizli"  # A "traktor" helyére a "fekete ribizli" kerül
print(gyumolcsok)
```

**Elem tartomány módosítása**

A lista egy adott tartománybeli elemeinek értékét úgy módosíthatjuk, hogy meghatározzuk az új értékek listáját, és hivatkozunk az indexek azon tartományára, ahová az új értékeket be szeretnénk szúrni:


```python
gyumolcsok = ["alma", "banán", "traktor", "narancs"]
gyumolcsok[1:3] = ["fekete ribizli", "dinnye"]  
print(gyumolcsok)
```
> Megjegyzések:
> * Ha több elemet szúrunk be, mint amennyit lecserélünk, az új elemek a megadott helyre kerülnek beillesztésre, a fennmaradó elemek pedig ennek megfelelően eltolódnak.
> * Ha kevesebb elemet szúrunk be, mint amennyit lecserélünk, az új elemek a megadott helyre kerülnek beillesztésre, a fennmaradó elemek pedig ennek megfelelően eltolódnak. A lista hossza ilyenkor megváltozik.

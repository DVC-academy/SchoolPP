# Függvények visszatérési értékkel

Ahogy a függvények pontban is láthatjuk, azt mondtuk, hogy a függvénynek adunk valamit, amire ő kidob valamit.
Az eddigi példákban viszont nem adtunk be semmit, és azon kívül, hogy kiírtunk valamit a konzolra, vissza sem igazán kaptunk semmit. Elszomorító... 😔

De ne csüggedjünk annyit, már itt is van a példa, hogy hogyan tudunk paramétereket átadni a függvénynek és kinyerni az eredményt:


```python
def add(a, b):
    result = a + b
    return result
```

- Ez az egyszerű kis függvényecske, annyit csinál, hogy összead két számot.
- `a` és `b` a függvény úgynevezett paraméterei
- A `result` nevű változóba mentjük az összeadás eredményét
- A `return` kulcsszó felel azért, hogy visszaadjunk a kapott eredményt

## Mit jelent az, hogy visszaadni?

Már mutatom is:
A feladat, hogy készíts egy számológépet, ami azért felel, hogy bármi történjen, mindenképp összeadjon két számot. Ennyi. Semmi mást nem fog csinálni. </br>
Vegyük végig lépésről lépésre, hogy mi történik ebben a kódrészletben:
- Először definiáljuk a függvényt, a már ismert módon.
- Ezután a `while 1` kifejezéssel létrehozunk egy végtelen ciklust. Ebből csak úgy tudunk kilépni, ha leállítjuk szín tiszta erőszakkal a program futását, magától sosem fog leállni. SOHA!!!
- Ezután bekérjük a 2 számot. FONTOS! Amit a konzolról bekérünk az mindig string típus lesz. Ezért, hogy összeadhassuk őket, valahogyan intekké kell varázsolnunk őket. Erre való az `int()` függvény. Amit paraméterként átadunk neki, abból megpróbál int-et készíteni.
- A következő sor a függvény hívás. Nagyon hasonló szintaxist láthatunk, mint amikor értéket adunk egy változónak. És lényegében ez is történik. Azt mondjuk a Python-nak, hogy az az érték, amit a függvény visszaad (ebben az esetben az összeadás eredménye) azt tárolja el a `final_result` nevű változóban.
- Végül pedig az eredményt kiírjuk a konzolra

```python
def add(a, b):
    result = a + b
    return result

while 1:
    first = int(input("Írd be az első számot:"))
    second = int(input("Írd be a második számot:"))
    final_result = add(first, second)
    print(f"Az összeadás eredménye: {final_result}")
```

Vegyük észre, hogy a változók nevei `first` és `second`, de a függvényen belül `a` és `b` a nevük. </br>
Python tudni fogja, hogy az első kapott paramétert (`first`) a függvényen belül `a`-ként kell kezelnie, a második paramétert (`second`) pedig `b`-ként.

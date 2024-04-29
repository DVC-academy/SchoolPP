# Integer

Programozásban az egész számokat `Integernek`, vagy röviden `int`-nek hívjuk. Ezek a pozitív vagy negatív egész számok, amelyek nem tartalmaznak törtrészt vagy tizedes pontot. Például:

```python
42
```

vagy 

```python
-7
```
Az egész számokat használhatjuk aritmetikai műveletekhez (pl. összeadás, kivonás, szorzás, osztás) és összehasonlításokhoz.

**Fontos!**

Ellentétben a string-ekkel, az int-eknél **NEM** használunk "" jeleket.

## Gyakori hibák

- Az egész számokat nem szabad idézőjelek közé tenni, mert akkor stringként értelmezi a Python.
> Példa: `"42"` - Ez egy string, nem egy egész szám.
> Ha összeadni próbáljuk egy másik egész számmal, akkor hibát fog kapni a program.
> Például:
> ```python
> "42" + 1
> ```
> Másold be ezt a kódot, és nézd meg, hogy mi lesz az eredménye!


- Az egész számokat nem szabad tizedes ponttal ellátni, mert akkor `float`-ként értelmezi a Python. (A float egy olyan adattípus, amely tizedes pontot tartalmaz, ezekről később lesz szó.)
> Példa: `42.` - Ez egy float, nem egy egész szám.
> Ha egy tizedes ponttal ellátott egész számot összeadni próbálunk egy másik egész számmal, bár nem kapunk hibát, de az eredmény nem int lesz.
> Például:
> ```python
> print(42 + 1.5)
> ```
> Könnyen beláthatjuk, hogy az eredmény nem egy egész szám, azaz nem int.


## Helyes használat

```python
intNumber = 42
name = "Vince"

print(f"Vince {intNumber} éves.")
```

Ebben a példában a `intNumber` változóban tároljuk az életkorunkat, és ezt kiírjuk a képernyőre a `print` függvény segítségével.
Láthatjuk, hogy a `intNumber` változó értéke nem idézőjelek között van, tehát az egy egész szám, nem egy string, ellentétben a `name` változóval.

### Emlékeztető kérdés
Mit jelent a `print(f"")` kifejezés? Miért jobb ez, mint a sima `print()`?
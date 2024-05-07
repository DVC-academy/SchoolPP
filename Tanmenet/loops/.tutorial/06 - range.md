# Range

**Mit tud igazán a range függvény?**

Ha a `range` függvénynek csak egy számot adsz, akkor 0-tól addig a számig számol.  Valójában azonban a `range` függvénynek több lehetősége is van:

* **Kezdő érték:**  Ezzel határozod meg, hogy melyik számtól kezdjen a számolás.
* **Végérték:**  Ez a szám egyel több, mint ameddig számolni szeretnél (például: ha a végértéket 10-nek adod meg, a számítógép 0-tól 9-ig számol).
* **Lépésköz:**  Ez határozza meg, hogy mennyit lépjen a ciklus minden egyes ismétlésénél (például: 1-es, 5-ös vagy 10-es lépésekkel szeretnél számolni?)

**Fontos megjegyezni:** A végértéknél van egy kimondatlan "kevesebb, mint" jel.  Ez azt jelenti, hogy a számítógép eggyel a megadott végérték előtt áll meg.

```python
range(<Kezdő érték>, <Végérték>, <Lépésköz>)
```

<details> <summary> Kezdő érték és végérték példák </summary>


**A tartomány első száma (100) a kezdőérték.**  A második szám (110) a végérték (ne feledd, hogy a végértéknek mindig eggyel többnek kell lennie, mint ameddig számolni szeretnél).

* **Melyik számot fogja először futtatni a kód? Melyik lesz az utolsó?**  Futtasd a kódot, és nézd meg!

```python
for i in range(100, 110):
  print(i)
```

**Mit gondolsz, mit fog kiírni a lenti kód? Futtasd le, és nézd meg!**

```python
for i in range(1, 7):
  print(f"{i}. Nap")
```

**Felfigyeltél, hogy a számláló a "6. napnál" leállt?**  Módosítsd a végértéket úgy, hogy eggyel több legyen, mint az utolsó kívánt szám - ebben az esetben 8, mert a hét 7 napját szeretnénk megjeleníteni.

```python
for i in range(1, 8):
  print(f"{i}. Nap")
```

**Mi történik, ha ezt a kódot futtatod?**

```python
print("7-es szozó tábla:")
for i in range(1, 10):
  print(i, "x 7 =", i * 7)
```

</details>

<details> <summary> Kezdő érték, végérték és lépésköz példák </summary>

**Számlálás felfelé lépésközzel:**

Képzelj el egy tartományt 0-nál kezdődik, és 999-ig (ami az írott végérték előtti szám) folytatódik. A számok minden alkalommal 25-ös lépésekben növekednek.

* **Milyen számokat vársz? Nyomd meg a futtatást, és nézd meg!**

```python
for i in range(0, 1000, 25):
  print(i)
```

**Visszaszámlálás:**

Ebben a példában 10-től kezdünk visszafelé számolni 0-ig (mert a 0 az, ami a felsorolt végérték előtti szám), és minden alkalommal 1-gyel lépünk visszafelé.

* **Mire számítasz, ha megnyomod a futtatást?**

```python
for i in range(10, -1, -1):
  print(i)
```

</details>
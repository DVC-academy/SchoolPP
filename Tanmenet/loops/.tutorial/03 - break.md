# Break utasítás

A `break` utasítás segítségével kiléphetsz a ciklusból. 

A kilépés azonnali, szóval ha a break után további kódok vannak írva a cikluson belül azok nem fognak lefutni.

A `break` után a számítógép rögtön a ciklus utánra ugrik.

`Futtasd` ezt a kódot, hogy lásd hogyan működik ez élesben!

```python
while True:
  print("Ez a program fut!")
  ujra = input("Futtassam újra?: ")
  if ujra == "nem":
    break
  print("Kár, pedig még akartam volna futni :/")
```
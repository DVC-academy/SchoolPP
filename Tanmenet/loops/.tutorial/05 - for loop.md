# For loop

A `while` ciklus tökéletes választás arra az esetre, amikor nem tudjuk előre, hányszor szeretnénk, hogy a ciklus lefusson.

Ha viszont van némi ötletünk a kívánt futtatások számáról, akkor a `for` ciklus ugyanúgy használható a kód ciklusonkénti futtatására, mint a `while` ciklus. A különbség az, hogy a `for` ciklusnál a változót, a vezérlési feltételt és a növelést mindössze EGY SORBAN állíthatjuk be.

## Összehasonlítás

Így hoztunk létre egy számlálót `while` ciklussal:

```python
counter = 0
while counter < 10:
  print(counter)
  counter += 1
```

Ugyanez a számláló `for` ciklussal:

```python
for counter in range(10):
  print(counter)
```

A fenti példában mindkét ciklus 0-tól 9-ig tízszer nyomtatja ki a számláló értékét. A különbség az, ahogyan a ciklust vezéreljük.

- A `while` ciklusnál egy változót ( `counter` ) hozunk létre, és inicializáljuk 0-val. A ciklus addig fut, amíg a `counter` értéke kisebb, mint 10. A ciklusmagban kiírjuk a `counter` értékét, majd növeljük 1-gyel a következő futtatáshoz.

- A `for` ciklusnál a `range(10)` kifejezést használjuk. A `range` függvény egy 0-tól 9-ig terjedő számsort generál (de nem tartalmazza a 10-et), ezt iteráljuk a ciklusban a `counter` változóval. A ciklus minden egyes futtatásánál a `counter` automatikusan a következő értéket veszi fel a számsorból, így nem kell külön léptetni. Mindössze annyit kell megadnunk, hogy hányszor szeretnénk, hogy a ciklus lefusson (a `range` függvényben a 10 a határ).

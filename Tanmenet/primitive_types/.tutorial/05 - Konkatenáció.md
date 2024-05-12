# Konkatenáció

Ha szeretnénk több változót egymás után fűzni (ez lehet bármilyen adattípus pl. string, int, saját típusok...), azt az alábbi módon tehetjük meg:

```python
first_part = "A szöveg első részéhez"
second_part = " a szöveg második részét fűzzük hozzá."
print(first_part, second_part)
```

A print() függvény az átadott paramétereket egymás után kiírja a konzolra. Ha vesszővel elválasztva több paramétert adunk át, akkor azokat szóközzel elválasztva írja ki.

### Mi a gond ezzel?

Ezt szeretném kiírni:
Szöveg első része: `Én vagyok a leg`
Szöveg második része: `jobb programozó a világon!`

Mi lesz ezzel a gomd, ha az előző példa szerint csináljuk?


<details> <summary> <b>Válasz</b></summary>
Sajnos szóközzel fogja őket összetenni: <br>
<b>Én vagyok a leg jobb programozó a világon</b>

Ez sajnos barátok között sem túl jó, nemhogy egy programban. <br>
A helyes megoldással már találkoztunk a kiíratásnál:

```python
first_part = "Én vagyok a leg"
second_part = "jobb programozó a világon!"
print(f"{first_part}{second_part}")
```
Ezzel a megoldással nem lesznek felesleges szóközök a két szöveg között.


</details>

# Konkatenáció

Ha szeretnénk több változót egymás után fűzni (ez lehet bármilyen adattípus pl. string, int, saját típusok...), azt az alábbi módon tehetjük meg:

```python
first_part = "Sziasztok"
second_part = "Vince vagyok"
print(first_part, second_part)
```

Ezzel csak annyi a gond, hogy automatikusan rak egy space-t a változóink értékei közé.

Tehát ha például van két változóm, amiből szeretnék egy számot összerakni helyiérték szerint:

```python
# 1-es helyiérték
num1 = 2
# 10-es helyiérték
num10 = 4
print("A szám:", num10, num1)
```

Az eredmény `A szám: 4 2` lesz, ami nekünk nem megfelelő.
Hogyan tudjuk elérni, hogy ne legyen space?

## Másik módszer a konkatenációra

Az alábbiakban láthatunk egy példát egy másik módszerre:

```python
print(f"{variable}")
```

Ebben az esetben a változókat nem egymás után tesszük vesszővel elválasztva, hanem kapcsos zárójelbe.

Így az előző példa az alábbi:
```python
print(f"A szám: {num10}{num1}")
```

<details><summary> Várt eredmény </summary>

`A szám: 42`
</details>
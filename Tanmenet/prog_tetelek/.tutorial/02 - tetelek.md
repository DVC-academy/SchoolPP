# Programozási tételek példákkal

### Sorozatszámítás (összegzés)
> Egy listához egy értéket rendelő feladattípusokhoz.
 

<details> <summary> Példa </summary>

```python
def sum_list(list):
  sum = 0
  for i in list:
    sum += i
  return sum

# Példa használat
list = [1, 2, 3, 4, 5]
sum = sum_list(list)
print(sum)  # Kiírja: 15
```

</details>

### Eldöntés
> Igazzal tér vissza, ha a listában létezik adott tulajdonságú elem, és hamissal ha nincsen ilyen a listában.

<details> <summary> Példa </summary>

```python
def contains_even_number(numbers):  
  for num in numbers:
    if num % 2 == 0:
      return True
  return False

# Példa használat
numbers = [1, 2, 3, 4, 5]
containsEven = contains_even_number(numbers)
print(f"Van-e páros szám a listában: {containsEven}")  # Kiírja: Van-e páros szám a listában: True
```
</details>

### Keresés
> Adott egy lista és egy, a lista elemein értelmezhető tulajdonság. A feladat az első elem indexének meghatározása melyre igaz az adott tulajdonság. Nem biztos, hogy a listában van ilyen elem. 

<details> <summary> Példa </summary>

```python
def get_first_even_number_index(numbers):
  for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
      return i
  return -1

# Példa használat
numbers = [1, 2, 3, 4, 5]
evenIndex = get_first_even_number_index(numbers)
print(f"Az első páros szám indexe a listában: {evenIndex}")  # Kiírja: Az első páros szám indexe a listában: 1
```
</details>

### Megszámolás
> Adott egy lista és egy, a lista elemein értelmezhető tulajdonság. Az a feladat, hogy az adott tulajdonsággal rendelkező elemek darabszámát meghatározzuk.

<details> <summary> Példa </summary>

```python
def count_even_numbers(numbers): 
  count = 0
  for num in numbers:
    if num % 2 == 0:
      count++
  return count

# Példa használat
numbers = [1, 2, 3, 4, 5]
numberOfEvens = count_even_numbers(numbers)
print(f"Ennyi páros szám van a listában: {numberOfEvens}")  # Kiírja: Ennyi páros szám van a listában: 2
```
</details>

### Maximum-minimum kiválasztás
> Adott egy nem üres lista. A feladat ezen lista legnagyobb (vagy legkisebb) elemének meghatározása. 

<details> <summary> Példa maximumra </summary>

```python
def get_max(numbers): 
  max = numbers[0]
  for num in numbers:
    if num > max:
      max = num
  return max

# Példa használat
numbers = [1, 2, 3, 4, 5]
max = get_max(numbers)
print(f"A legnagyobb szám a listában: {max}")  # Kiírja: A legnagyobb szám a listában: 5
```
</details>

<details> <summary> Példa minimumra </summary>

```python
def get_min(numbers): 
  min = numbers[0]
  for num in numbers:
    if num < min:
      min = num
  return min

# Példa használat
numbers = [1, 2, 3, 4, 5]
min = get_min(numbers)
print(f"A legkisebb szám a listában: {min}")  # Kiírja: A legkisebb szám a listában: 1
```
</details>

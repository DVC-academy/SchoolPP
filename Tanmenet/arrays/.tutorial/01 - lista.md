# Listák

A listák több elemet tárolnak egyetlen változóban.

A listák a Python négy beépített adattípusa közül az egyik, amely adatkollekciók tárolására szolgál. A másik három a **Tuple**, a **Set** és a **Dictionary**, mindegyik különböző tulajdonságokkal és használattal rendelkezik, később részletesen is lesz róluk szó.

Listák szögletes zárójelekkel hozhatók létre:

Példa:
```python
my_list = ["alma", "banán", "traktor", "alma"]  # Lista létrehozása
print(my_list)  # A lista elemeinek kiíratása
```

## Tulajdonságok

A listaelemek rendezettek, módosíthatók, és lehetővé teszik az ismétlődő értékeket.

 **Rendezett**  
> Amikor azt mondjuk, hogy a listák rendezettek, az azt jelenti, hogy az elemeknek meghatározott sorrendje van, és ez a sorrend nem változik magától. 
> Új elemek hozzáadásakor azok a lista végére kerülnek. 
> Fontos megjegyezni, hogy vannak olyan lista metódusok, amelyek megváltoztathatják a sorrendet, de általánosságban az elemek sorrendje megmarad.

**Módosítható**
> A lista módosítható, ami azt jelenti, hogy a létrehozás után megváltoztathatjuk, hozzáadhatunk és eltávolíthatunk elemeket a listából.

**Duplikátumok engedélyezettek**
> Mivel a listák indexeltek, azonos értékek is szerepelhetnek a listában.

A listaelemek indexeltek, az első elem indexe `[0]`, a második elem indexe `[1]` stb. 

A listaelemek különböző típusúak is lehetnek.

```python
my_list = ["traktor", True, 42, "traktor"]  
print(my_list[0]) # 1. elem
print(my_list[1]) # 2. elem
print(my_list[2]) # 3. elem
print(my_list[2]) # 4. elem
```

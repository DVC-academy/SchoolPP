# Lista olvasása

Az alap indexelésen felül használhatunk egyéb indexelési formákat is.

## Negatív indexelés

A negatív indexelés azt jelenti, hogy a lista végéből kezdünk számolni.

* A `-1` az utolsó elemre mutat,
* a `-2` a második utolsó elemre,
* és így tovább.

Lista utolsó elemének kiíratása:

```python
my_list = ["traktor", True, 42, "másik traktor"]  
print(my_list[-1]) 
```

## Index tartomány

Index tartományt úgy határozhatunk meg, hogy megadjuk a kezdő és a záró indexet.

Tartomány megadásakor a visszatérési érték egy új lista lesz a megadott elemekkel.

A harmadik, negyedik és ötödik elem kiíratása:

```python
my_list = ["traktor", True, 42, "traktor", "ötödik elem", "hetedik előtti elem"]  
print(my_list[2:5]) 
```

### Kezdőérték kihagyása

Ha kihagyjuk a kezdőértéket, a tartomány az első elemtől kezdődik:

```python
my_list = ["traktor", True, 42, "traktor", "ötödik elem", "hetedik előtti elem"] 
print(my_list[:4]) 
```

### Záróérték kihagyása

Ha kihagyjuk a záróértéket, a tartomány a megadott index utáni összes elemet tartalmazza a lista végéig:

```python
my_list = ["traktor", True, 42, "traktor", "ötödik elem", "hetedik előtti elem"] 
print(my_list[2:]) 
```

> Megjegyzés: a tartományok negativ indexekkel is működnek (pl: `[-4:-1]`)
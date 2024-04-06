# Változók

Programozásban változókat használunk az adatok eltárolására. Ha például azt szeretnénk, hogy a program megjegyezze azt a string-et amit megadtam neki (például a nevemet), akkor egy változóba el tudom azt menteni. Az alábbi sorban láthatunk erre egy példát:

```python
name = "Alex"
```

Ahogy a fenti példában látható, egy változó érték adásának 3 része van.

### name 
A változó neve. A későbbiekben ha szeretnénk felhasználni a változóba elmentett értéket, akkor erre a névre kell majd hivatkoznunk. Ez bármi általunk válaszott szó lehet, érdemes olyat választani, amiből egyértelműen tudjuk, hogy az adott változónak mi az értéke.

### =
Az egyenlőség jel a programozásban (matematikával ellentétben) az értékadás jele. Ez eddig tehát azt jelenti, hogy a **name** nevű változó értéke **LEGYEN**. 

### "Alex"
A változó értéke. Amikor a **name** nevű változóra hivatkozunk, akkor valójában mi ezt az értéket szeretnénk visszakapni.
Így hangzik tehát a teljes parancs:
A **name** nevű változó értéke legyen **Alex**

## A változók szintaxisa
> Emlékeztető: A szintaxis a programozási nyelvben használt szabályok rendszere, amely meghatározza, hogy hogyan kell helyesen megírni a kódot.

Pythonban a válozók névadásánál az alábbiakra kell figyelnünk:
1. A változó neve legyen egyértelmű, ne zavarjuk össze saját magunkat és másokat.
  Jó példa:
  ```python
  fruit = "Apple"
  ```
  Rossz példa:
  ```python
  x = "Pear"
  ```
  Ebben az esetben a fruit nevű változóról gyaníthatjuk, hogy valamilyen gyümölcsnév lesz a tartalma, míg az x esetében gondolhatunk pl. egy egyenlet megoldására, vagy egy koordinátára, de semmiképp sem egy gyümölcsre.
   
2. Ha a változó neve több szóból áll, akkor a különböző szavak elválasztására használjunk alulvonást (snake_case).

```python
my_favorite_number = 15
```

> Megjegyzés: Ezek csupán irányelvek, a program ugyanúgy fog működni akkor is, ha nem tartjuk be ezeket a szabályokat, azonban a kód nehezebben lesz olvasható mások számára (illetve saját magunk számára is...)

3. A változók neve case-sensitive, ami azt jelenti, hogy különbséget tesz kis és nagybetűk között.

Tehát a **my_variable** és a **my_Variable** változónevek NEM azonosak.

4. Kerüljük azokat a változóneveket, amiket a Python alapból is használ (egyre több ilyennel találkozunk majd).

5. A Python változók nevei csak betűvel, vagy alulvonással kezdődjenek.

6. A változók nevei tartalmazhatnak kis- és nagybetűket (a-z, A-Z), számokat (0-9) és alulvonást (_). (Persze mindezeket úgy, hogy közben betartjuk az eddigi pontokban megfogalmazottakat)
    
7. A változók neve NEM kezdődhet számmal
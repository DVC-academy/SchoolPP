# Mi az a git?


### Példa
Képzeljük el, hogy Dávid és Vince ugyanazon a kódon dolgoznak. Ideális esetben ez a párbeszéd zajlik le köztük az irodában: </br>

- Szevasz Dávid!
- Szia Vince, mi a helyzet?
- Minden oké kicsit rossz napom volt...
- Aha, az tök jó, beszélünk kicsit a kódról?
- ... igen 😔
- Szóval van egy függvény a 7-edik sorban, aminél megváltoztatnám a szöveget úgy, hogy azt írja ki a konzolra, hogy: Szeretem az őszt!
- Húú de jó, hogy mondod, én is pont ezt akartam megváltoztatni, csak Szeretem a tavaszt-ra.

És a történet úgy ér véget, hogy megbeszélik melyik a megfelelőbb mondat, és azt választják. </br>

`De sajnos az élet nem ilyen egyszerű.`

### Életszerűbb példa:

Vince és Dávid egy hónapja nem voltak bent az irodában, nem is találkoztak. Mind a ketten megkapták a kódot, és elkezdtek rajta dolgozni.
Dávid megírta a kódját `Szeretm az őszt` szöveggel, Vince pedig `Szeretem a tavaszt` szöveggel.
Amikor egy hónap után bemennek az irodába, ott szembesülnek vele, hogy valamelyikük feleslegesen dolgozott. </br>
Ezt a pici problémát viszonylag könnyen meg tudják oldani, de felmerül a kérdés, nem lehetett volna ezt elkerülni?

<details><summary> Válasz </summary>

**De igen**

</details>

## Miért segít ebben a git?

A git egy úgynevezett verziókezelő rendszer. Arra szolgál, hogy ha sok ember (lehet 2-3, de akár több 100 is) együtt dolgozik, esetlegesen ugyanazokon a fájlokon, akkor se legyen semmi probléma. </br>
A git további funkciói, amiért nagyon szeretjük:
- `Verziókövetés:` A git segítségével nyomon tudjuk követni, hogy milyen változtatásokat hajtottunk végre a kódunkon. Ez olyan, mint amikor egy rajzot készítesz, és minden egyes változtatást lefényképezel, hogy később visszanézhesd, hogyan alakult a rajzod.
- `Együttműködés:` A git segítségével több ember is tud dolgozni ugyanazon a projekten anélkül, hogy összezavarnák egymást. Ez olyan, mint amikor többen is rajzoltok ugyanarra a papírra, de mindenki a saját részén dolgozik, és a végén összeillesztitek a részeket.
- `Biztonság:` Ha valami rosszul sül el a kódunkban, a git segítségével vissza tudunk térni a korábbi, működő verzióhoz. Ez olyan, mint amikor egy játékban elrontasz valamit, de van egy mentésed, amit vissza tudsz tölteni, hogy újra próbálkozhass.
- `Kód megosztása:` A git segítségével könnyen meg tudjuk osztani a kódunkat másokkal.
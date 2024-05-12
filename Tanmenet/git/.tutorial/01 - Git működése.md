# Git működése

Az alábbi ábra egy kis segítség, ha megzavarodnánk, hogy mi hogyan működik:

![git workflow](img/git.jpeg)

## Repository

## Local
Git-ben `repository`-nak nevezzük a projektünket. Tehát ha egy új projektet indítok, és azt szeretném, 
hogy Gitet használjon, akkor létrehozok a számítógépemen egy Git projektet
(később részletezzük, hogy hogyan). Innentől kezdve erre hivatkozhatunk úgy, hogy `local repository` (a képen `localrepo`).
Ez annyit jelent, hogy az adott kód a számítógépen van. Tehát ha tönkremegy a gépem, és elvesznek az adatok, akkor végleg elvesztek.
Mit tehetnék, hogy ne vesszenek el?

## Remote

Ha azt szeretnénk, hogy a kódunk mások számára is elérhető legyen, vagy nem szeretnénk,
hogy elvesszen pl. ha tönkre megy a gépünk, akkor használhatjuk a Git `remote repository` (a képen `remote repo`) funkcióját. 
Ehhez szükségünk lesz egy Git-et kezelni tudó alkalmazásra, az egyik legnépszerűbb a `Github`, mi is ezt fogjuk használni.

## Push, pull

Nézzünk egy gyakorlati példát. Létrehoztam a számítógépemen egy projektet, amiben Git-et használok verziókezelésre,
és github-ra szeretném majd elmenteni a változtatásaim.
A kódom az alábbi:

```python
print("Hello World!")
```

Mivel ez életem munkája, semmiképpen sem szeretném ha elveszne, így `push`-olom a remote repository-ba. 
Innentől kezdve a kódom elérhető lesz mások számára is, illetve szerencsére nekem is. </br>

Ugyanis sajnos ellopták a gépemet, ezért újat kellett vásárolnom. Az új projekten értelemszerűen nincsen rajta a kód,
amit írtam, de egy percig sem szomorkodom, hiszen használtam git-et. Hogyan fogom tudni vissza szerezni? </br>

A `pull` paranccsal. Egy pillanat alatt le is tölti a git a korábban `push`-olt kódomat,
és ott folytathatom ahol abbahagytam.

Ezek a Git legfontosabb funkciói, a további részletekről a következő füleken olvashatsz!


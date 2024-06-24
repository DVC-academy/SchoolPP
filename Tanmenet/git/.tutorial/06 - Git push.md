# Git push

Ha szeretnénk a commit-jainkat, és ezzel a kódunk aktuális állapotát elmenteni azt a `git push` paranccsal tehetjük meg.
Ez a parancs fel fogja push-olni a változtatásainkat a kiválasztott repository-ba, esetünkben a Github-ra.

## Hova is fogunk push-olni?

Könnyű azt mondani, hogy mi Github-ra push-olunk, a gond csak az, hogy a számítógépünkön ezt nem mondtuk meg a Git-nek.
Így ha kiadjuk a `git push` parancsot, az alábbi üzenetet kapjuk:
![1wrong-push](img/06-git-push/1.wrong-push.png) <br>

Ez azért történik, mert bár mi a saját gépünkön létrehoztuk a projektet, a Github erről mit sem tud.
> (továbbra se felejtsük el, a Git egy szoftver ami a verziókövetésért felel, a Github pedig egy web alkalmazás,
ami szintén Git-et használ, és segít nekünk a projektjeink kezelésében)

A 2-es pontban már láttuk, hogy hogyan tudunk létrehozni Github-on egy repository-t. 
Jelenleg a helyzet az, hogy van egy üres Github repository-nk, és egy lokális Git projektünk,
de a kettő nem tud egymásról. A fenti hibaüzenet erre vonatkozik. A következőkben, össze fogjuk kötni a kettőt.
> VIGYÁZZ! Ez a parancs változhat attól függően, hogy mi a felhasználóneved Github-on, 
> és hogy milyen nevet adtál a repositorydnak. 

Az alábbi példában a felhasználónév `vasvince98`, a projekt neve pedig `hello-git`. Ezért a parancs a következő:

`git remote add origin git@github.com:vasvince98/hello-git.git`

Amennyiben a felhasználónév `teszt.elek69` a repository neve pedig `my-own-nasa`, akkor a parancs a következő:

`git remote add origin git@github.com:teszt.elek68/my-own-nasa.git`

Nagyon figyeljünk, hogy helyes adatok legyenek megadva, különben nem fog működni.



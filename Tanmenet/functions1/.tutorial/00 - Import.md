# Import

## Python modul
Pythonban használhatunk mások által már előre megírt kódokat.
Például ha szeretnénk megtudni mennyi az idő, nem kell kitalálnunk, hogy hogyan kell kiszámolni, hanem használhatjuk a `datetime` modult.

```python
import datetime

print(datetime.datetime.now())
```

Az import kulcsszóval megmondjuk a Pythonnak, hogy melyik modult szeretnénk használni. A `datetime` modulban található `datetime` osztályt használjuk, hogy kiírassuk az aktuális dátumot és időt. </br>
Nem baj, ha még nem értjük teljesen a kódot, a lényeg, hogy lássuk, hogy hogyan kell használni egy olyan modult, amit nem mi írtunk.
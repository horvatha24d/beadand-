# gyak0415.py

class Diak:
    def __init__(self, nev, osztaly, atlag):
        self.nev = nev
        self.osztaly = osztaly
        self.atlag = float(atlag)

# Fájl beolvasása
diakok = []
with open('diak.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split(';')
        if len(parts) == 3:
            nev, osztaly, atlag_str = parts
            diak = Diak(nev.strip(), osztaly.strip(), atlag_str.strip())
            diakok.append(diak)

# 1. Hány fős a csoport?
print("A csoport", len(diakok), "fős.")

# 2. Csoportátlag
osszeg = sum(d.atlag for d in diakok)
csoportatlag = osszeg / len(diakok)
print("A csoport átlaga:", csoportatlag)

# 3. Legjobb tanuló
legjobb = max(diakok, key=lambda d: d.atlag)
print("A legjobb tanuló:", legjobb.nev, "átlaga:", legjobb.atlag)

# 4. Évfolyamok ellenőrzése 9-12-ig
evfolyamok = set()
for d in diakok:
    evfolyam = d.osztaly[0:2]
    evfolyamok.add(evfolyam)

minden = {'09', '10', '11', '12'}
hianyak = minden - evfolyamok
if not hianyak:
    print("9-12-ig minden évfolyamról van tanuló a csoportban.")
else:
    print("Hiányzó évfolyam(ok):" ,  ', '.join(hianyak))
    

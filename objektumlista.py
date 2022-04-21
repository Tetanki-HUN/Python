

class Nobeldijak:
    ev: int
    nev: str
    szulhal: str
    orszag: str
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.ev = int(adatok[0])
        self.nev = adatok[1]
        self.szulhal = adatok[2]
        self.orszag = adatok[3]
        
file = open('orvosi_nobeldijak.txt', 'r', encoding='utf-8')

osszesNobeldijas: list[Nobeldijak] = []

file.readline()
for sor in file:
    egyEmber = Nobeldijak(sor.strip())
    osszesNobeldijas.append(egyEmber)

print(osszesNobeldijas[10].nev)

for egy in osszesNobeldijas:
    print(egy.ev)
    
for i in range (len(osszesNobeldijas)):
    print(osszesNobeldijas[i].nev)
    
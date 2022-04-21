'''
Osztály létrehozása
'''
from msilib.schema import File


class Eredmeny:
    nev: str
    rajtszama: int
    kategoria: str
    ido: str
    tavszazalek: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.rajtszama = int(adatok[1])
        self.kategoria = adatok[2]
        self.ido = adatok[3]
        self.tavszazalek = int(adatok[4])

file = open('ub2017egyeni.txt', 'r')

noidb = 0
minSzazalak = 100

file.readline()
for sor in file:
    #összes sor kiírása
    print(sor)
    #egyAdat nevű Eredmkény típusú objektum létrehozása
    egyAdat = Eredmeny(sor)
    print("Neve: ", egyAdat.nev, " ideje: ", egyAdat.ido)
    #Hány nő van?
    if egyAdat.kategoria == "Noi":
        noidb = noidb + 1
    #Hány %-ot teljesített a leghamarabb teljesítő?
    if egyAdat.tavszazalek < minSzazalak :  
        minSzazalak = egyAdat.tavszazalek
        
print(minSzazalak)
print(noidb)
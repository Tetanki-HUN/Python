from posixpath import split


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
'''
Hány Nobel díjas van?
Hány magyar Nobel díjas van? (magyar = H)
Mikor kapták az első Nobel díjat?
Szerepel-e a listában Otto nevű ember?

'''

nobeldijas = 0
magyardijas = 0
minEv = 2000

file.readline()
for sor in file:
    print(sor)
    egyEmber = Nobeldijak(sor)
    print("Neve: ", egyEmber.nev,)
    #Hány Nobel díjas van?
    nobeldijas = nobeldijas + 1
    

    #Hány magyar Nobel díjas van?
    if egyEmber.orszag == "H":
        magyardijas = magyardijas + 1
        
        
    #Mikor volt az első Nobel díj átadása?
    if egyEmber.ev < minEv:  
        minEv = egyEmber.ev
        
    
    #Szerepel-e a listában Otto nevű ember?
    file.seek(0)
    file.readline()
    szerepel = False
    for sor in file:
        egyEmber = Nobeldijak(sor.strip())
        if ("Otto" in egyEmber.nev):
            szerepel = True
    if szerepel:
        print("Szerepel Otto nevű")
    else:
        print("Nem szerepel Otto nevű")
    
    file.seek(0)
    file.readline()
    for sor in file:
        egyEmber = Nobeldijak(sor.strip())
        evek = egyEmber.szulhal.split("-")
        if(evek[1] != ""):
            print(egyEmber.nev, ": ", int(evek[1])-int(evek[0]))
    

print(nobeldijas)
print(magyardijas)
print(minEv)
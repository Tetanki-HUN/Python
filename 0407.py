from operator import index
from turtle import st

class Eredmeny:
    nev: str
    rajtszam: int
    kategoria: str
    ido: str
    tavszazalek: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        self.ido = adatok[3]
        self.tavszazalek = int(adatok[4])
        
file = open('ub2017egyeni.txt', 'r')
'''
1. Számolja meg és írja ki a képernyőre a minta szerint, hogy hány női sportoló teljesítette a 
teljes távot!
2. Kérje be a felhasználótól 1 sportoló nevét, majd határozza meg és írja ki a minta szerint,
a sportoló indult-e a versenyen! Ha a sportoló indult a versenyen, akkor azt is írja ki a 
képernyőre, hogy a teljes távot teljesítette-e! (Feltételezheti, hogy nem indultak azonos nevű
sportolók ezen a versenyen.)
3. Írassa ki az első sportoló idejét órában! Pl 1:30:00 -> 1,5
4.Készítsen egy függvényt (idoOraban), ami megkapja a versenyző időeredményét majd visszaadja 
az időt órában! Pl, 1:30:00 -> 1,5
5. Határozza meg és írja ki a minta szerint a teljes távot teljestő férfi sportolók átlagos
idejét órában! Feltételezheti, hogy legalább egy ilyen sportoló volt. (28,347)
'''

osszesEredmeny = []
noiteljesitok: 0

for sor in file:
    egyEredmeny = Eredmeny(sor.strip())
    osszesEredmeny.append(egyEredmeny)

print("A listában", len(osszesEredmeny), " eredmény van")


'''
1. Számolja meg és írja ki a képernyőre a minta szerint, hogy hány női sportoló teljesítette a 
teljes távot!
'''
for egyAdat in osszesEredmeny:
    if egyEredmeny.kategoria == "Noi" and egyEredmeny.tavszazalek == 100:
        noiteljesitok = noiteljesitok + 1

print(noiteljesitok)

'''
2. Kérje be a felhasználótól 1 sportoló nevét, majd határozza meg és írja ki a minta szerint,
a sportoló indult-e a versenyen! Ha a sportoló indult a versenyen, akkor azt is írja ki a 
képernyőre, hogy a teljes távot teljesítette-e! (Feltételezheti, hogy nem indultak azonos nevű
sportolók ezen a versenyen.)
'''



'''
3. Írassa ki az első sportoló idejét órában! Pl 1:30:00 -> 1,5
'''
ido = osszesEredmeny[0].ido.split(":")
oraban = (int(ido[0]))*3600 + int(ido[1])*60 + int(ido[2]) / 3600
print(oraban)

'''
4.Készítsen egy függvényt (idoOraban), ami megkapja a versenyző időeredményét majd visszaadja 
az időt órában! Pl, 1:30:00 -> 1,5
'''
def idoOraban(idoString: st) -> float:
    ido = idoString.split(":")
    
    ora = (int(ido[0]))*3600 + int(ido[1])*60 + int(ido[2]) / 3600
    return ora
print(idoOraban(osszesEredmeny[0].split))

'''
5. Határozza meg és írja ki a minta szerint a teljes távot teljestő férfi sportolók átlagos
idejét órában! Feltételezheti, hogy legalább egy ilyen sportoló volt. (28,347)
'''

ferfidb: 0

for egyAdat in osszesEredmeny:
    if egyAdat.kategoria == "Ferfi" and egyAdat.tavszazalek == 100:
        ferfiido = (int(ido[0]))*3600 + int(ido[1])*60 + int(ido[2]) / 3600
        ferfidb = ferfidb + 1

print(ferfiido)
print(ferfidb)

'''
6. Hány célbaérkezett versenyző van aki előtte és utána nem teljesítette: 
'''

elottautana: 0

for i in range(1,len(osszesEredmeny)-1):
        if osszesEredmeny[i].tavszazalak == 100 and osszesEredmeny[i-1].tavszazalak < 100 and osszesEredmeny[i+1].tavszazalak > 100:
            elottautana = elottautana + 1
        
print(elottautana)       

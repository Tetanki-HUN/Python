from fileinput import close


class Foci:
    fordulo: str
    hazaig: int
    vendegg: int
    hazaifelg: int
    vendegfelg: int
    hazaics: str
    vendegcs: str
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.fordulo = adatok[0]
        self.hazaig = int(adatok[1])
        self.vendegg = int(adatok[2])
        self.hazaifelg = int(adatok[3])
        self.vendegfelg = int(adatok[4])
        self.hazaics = adatok[5]
        self.vendegcs = adatok[6]
        

file = open('meccs.txt', 'r')

file.readline()

osszesEredmeny = []

for sor in file:
    egyEredmeny = Foci(sor.strip())
    osszesEredmeny.append(egyEredmeny)


'''
1. feladat.
Írassuk ki hogy összesen hány meccs volt
'''
print("A listában ", len(osszesEredmeny), " mérkőzés van.")


'''
2. feladat.
Kérjünk be egy fordulót, és írjuk ki az adatait!
'''
keresettFordulo = input("Add me egy forduló sorszámat 1-20 között: ")

for Foci in osszesEredmeny:
    if Foci.fordulo == keresettFordulo:
        print(Foci.hazaics, "-",Foci.vendegcs, ": ",Foci.hazaig, "-" ,Foci.vendegg, " A félidőben meg: ",Foci.hazaifelg, "- ",Foci.vendegfelg)
        
        
        
'''
3. feladat.
Kérjünk be egy csapat nevet, és válaszoljunk, hogy volt-e ilyen a mérkőzéssorozatban
'''

keresettcsapat = False
for Foci in osszesEredmeny:
    if Foci.hazaics or Foci.vendegcs == keresettcsapat:
        keresettcsapat = True

if keresettcsapat == True:
    print(keresettcsapat, "szerepelt a mérkőzésekben.")
    
   
 
'''
4. feladat.
Határozza meg, hogy a bajnokság során mely csapatoknak sikerült megfordítaniuk az állást
Ez azt jelenti, hogy a csapat az első félidőben vesztésre állt ugyan, de sikerült a megnyerniük a mérkőzést.
A képernyőn soronként tüntesse fel a forduló sorszámáz és a győztes csapat nevét!
'''    


for Foci in osszesEredmeny:
    if Foci.hazaig - Foci.hazaifelg > Foci.vendegg - Foci.vendegfelg:
        print(Foci.fordulo, "A nyertes csapaz: ",Foci.hazaics)
    elif Foci.hazaig - Foci.hazaifelg < Foci.vendegg - Foci.vendegfelg:
        print(Foci.fordulo, "A nyertes csapaz: ",Foci.vendegcs)
     



'''
5. feladat.
Hány gólt lőttek a Nyulak(csapat) vendégként
'''


Nyulakg = 0
for Foci in osszesEredmeny:
    if Foci.vendegcs == "Nyulak":
        Nyulakg = Nyulakg + Foci.vendegg

print("A Nyulak vendegcsapatkent ",Nyulakg," szereztek!")




'''
6. feladat.

'''





file = close
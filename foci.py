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
    
print("A listában ", len(osszesEredmeny), " mérkőzés van.")
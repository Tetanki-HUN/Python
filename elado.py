class Elado:
    eladott: int
    hossz: str
    fizetendo: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.eladott = int(adatok[0])
        self.hossz = adatok[1]
        self.fizetendo = int(adatok[2])        
        
file = open('eladott.txt', 'r')

osszesEladas = []

for sor in file:
    egyEladas = Elado(sor.strip())
    osszesEladas.append(egyEladas)
    
print(osszesEladas)

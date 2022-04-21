'''
Kutya osztály létrehozása
'''
class Kutya:
    nev: str
    fajta: str
    szulIdo: int
    
    def __init__(self, neve: str, fajtaja: str, szulIdeje: int) -> None:
        self.nev = neve
        self.fajta = fajtaja
        self.szulIdo = szulIdeje
        
    def ugat(self):
        print("Vau vau...")

'''
Kutya osztályú objektumok létrehozása (példábnyosítás) -> konkrétan 1 kutya
'''
enKutyam = Kutya("Bodri", "puli", 2020)
print(enKutyam.nev)
print("Kora: ",2022-enKutyam.szulIdo)

teKutyad = Kutya("Zeusz","német juhász", 2020)
print("A te kutyád neve: ", teKutyad.nev, ", fajtája ", teKutyad.fajta, " és születési éve ", teKutyad.szulIdo)

'''
A Kutya osztály metódusának hívása 
'''


'''
Hozz létre Autó osztályt
Tulajdonságai:
márka
évjárat
szín
hengerűrtartalom

Metódusai:
(kunstruktor)
dudál
'''

class Auto:
    marka: str
    evjarat: int
    szin: str
    hengerurtartalom: str

    def __init__(self, markaja: str, evjarata: int, szine: str, hengerurtartalma: str) -> None:
        self.marka = markaja
        self.evjarat = evjarata
        self.szin = szine
        self.hengerurtartalom = hengerurtartalma

    def hang(self):
        print("Yes yes")

enAutom = Auto("Ben", 2019, "Szürkés-barna", 1300)
print(enAutom.marka)
print("Az én autóm márkája:", enAutom.marka, ", évjárata ", enAutom.evjarat, ", a színe ", enAutom.szin, " és végül hengerűrtartalma ", enAutom.hengerurtartalom)

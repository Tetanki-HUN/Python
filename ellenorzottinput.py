#Feladat
#Addig kérjük be a felhasználótól egy számot,
#amíg 1 és 20 közötti párosat nem ad meg.

szam = int(input('Mondj nekem egy egész számot: '))

while (szam > 1 and szam < 20 and szam%2 == 1):
    print('A számod az én gondolt számaim kívűl van, vagy páratlan. (Nem szeretem a páratlan számokat UnU)')
    
print('A számod az én gondolt számaim között van és egyébként páros is. :D')   


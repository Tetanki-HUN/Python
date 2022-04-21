#Írjuk ki 10-szer egymás után alá hogy helló

A = 0

while A != 10:
    A += 1
    print("Helló!")


B = int(input('Mondanál egy számot? '))

db = 0


while B < 1000:
    B *= 2
    print(B)
    db = db + 1

print(db)

C = int(input('Mondanál újra egy számot? '))

bd = 0


while C < 1000:
    C *= 2
    print(C)
    if C % 3 == 0:
        bd += 1

print(bd) 
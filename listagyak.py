'''
Lista létrehozása
'''
szamok = [69, 420, 3]
print(szamok)

'''
Adjunk hozzá 2 új számot 
'''
szamok.insert(len(szamok), 4)
szamok.insert(len(szamok), 5)
print(szamok)

'''
Hány db páros szám van a listában?
'''
db = 0
for i in range(len(szamok)): 
    if szamok[i]%2 ==0:
        db = db + 1
print(db, " db páros szám van a listában")

'''
Ha a szám kisebb 5-nél, szorozza 2-vel
egyébként ossza hárommal
'''

for i in range(len(szamok)): 
    if szamok[i] < 5:
        szamok[i] = szamok[i]*2
    else: szamok[i]=szamok[i]/3
print(szamok)

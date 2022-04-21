#A szám 10 és 20 között van
print("Helló!")
A = input('Mondanál egy számot?')
if A>10 | A<20: print('A számod 10 és 20 között van.')
else: print('A számod 10 alatt vagy 20 felett van.')

#A szám nagyobb 10-nél és osztható 4-gyel?
B =input('Mond egy számot 10 felett')
if B > 10 & B / 4 == 0: print('A számod osztható 4-gyel és 10 felett is van.')
else: print('A számod 10 alatzt van vagy 10 felett de nem osztható 4-gyel.')

#A szám kisebb 20-nál és osztható 2-vel vagy 3-mal
C =input('Mond egy számot 10 és 20 között')
if C < 20 & C / 2 == 0 | C / 3 == 0: print('A számod osztható 2-vel vagy 3-mal és 20 alatt is van.')
else: print('A számod 20 felett van vagy nem osztható 2-vel vagy 3-mal.')
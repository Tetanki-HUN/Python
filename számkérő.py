#páratlan 1 és 20 között van kiírja a feltétel igaz
import math
print('Gondoltam 2 számra :D')
A = int(input('Mondj nekem egy egész számot: '))

if (A>= 1 and A <= 20 and A%2 == 1):
    print('A számod az én gondolt számaim között van és egyébként páratlan is. :D')

else:
    print('A számod az én gondolt számaim kívűl van, vagy páros. (Nem szeretem a páros számokat UnU)')
    
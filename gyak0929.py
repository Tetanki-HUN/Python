import math
A = int(input('Mondj nekem egy egész számot: '))
B = int(input('Mondj nekem még egy egész számot: '))

#A négyzet + B négyzet a C
C= math.sqrt((A*B) + pow(A*2,2))
if 0>C:
    print('A megoldás' ,C,)

else: 
   print('Nincs megoldás.')
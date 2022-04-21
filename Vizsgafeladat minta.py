import math


a = int(input('Mondj nekem egy egész számot: '))
b = int(input('Mondj nekem még egy darab egész számot: '))

'''
^Megadjuk a 2 számot^
'''

if b == a:
    print("Szerintem " ,b, " egyenlő " ,a, )
elif b > a:
    print("Szerintem " ,b, " nagyobb mint " ,a, )
else:
    print("Szerintem " ,a, " nagyobb mint " ,b, )
    
'''
^Kiírassuk a nagyobb/kisebb/egyenlő számot^
'''

haromszog1 = int(input('Mond meg nekem a háromszög eggyik oldalát : '))
haromszog2 = int(input('Mond meg nekem a háromszög a 2. oldalát: '))
haromszog3 = int(input('Mond meg nekem a háromszög a 3. oldalát: '))

'''
^Megadjuk a háromszög oldalainak hosszát^
'''
if haromszog1 + haromszog2 == haromszog3:
    print("A háramszög szerkezthető")
elif haromszog3 + haromszog2 == haromszog1:
    print("A háramszög szerkezthető")
elif haromszog1 + haromszog3 == haromszog2:
    print("A háramszög szerkezthető")
else:
    print("A háromszög nem szerkezthető")
    
'''
^Kiírassuk hogy a háromszög szerkezthető e vagy sem^
'''


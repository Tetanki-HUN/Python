from operator import truediv
from random import random
import re

from xmlrpc.client import INVALID_METHOD_PARAMS, boolean

szam = input("Mondj nekem egy darab számot kérlek! ")
def prime(szam: int) -> boolean:
    osztok = 0
    for i in range(szam):
        if szam%(i+1) == 0:
            osztok = osztok + 1
    return osztok == 2

lista = []
for i in range(10):
    lista.append(random.randint(10,99))
    print(lista[i])
    
'''
Eldöntöm hogy van a listában van-e prímszám 
'''
'''
Első verzió
'''
vanebenneprim = False
for i in range (10):
    if(prime(lista[i])):
        vanebenneprim= True
if vanebenneprim == True:
    print("Van benne prím")
else:
    print("Nincs benne prím")        
'''
Második verzió
'''
primdb = 0
for i in range(10):
    if(prime(lista[i])):
        primdb = primdb + 1
        
'''
Egy szóban meghatározza a magánhangzók számát
'''

szo = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
magánhangzók: int = 0
mgh = "aáeéiíoóöőuúüű"
for i in range(len(szo)):
    if szo[i] in mgh:
        magánhangzók = magánhangzók + 1 
else:
    print((),magánhangzók, "darab magánhangzó van a(z)" ,szo, "szóban")

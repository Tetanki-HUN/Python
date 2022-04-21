from random import random
from xmlrpc.client import boolean


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
    
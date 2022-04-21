from re import I
from xmlrpc.client import boolean


evszam = input("Mondanál nekem egy évszámot légyszíves: ")

def szokoev(evszam: int) -> boolean:
    return evszam/400 == 0 or evszam/4 == 0 and evszam/100 != 0

ev1: int = int(input("Melyik évtől számoljuk? "))
ev2: int = int(input("Meddig számoljuk? "))
db = 0

for ev in range(ev1, ev2 + 1):
    if szokoev(ev):
        print(ev)
        db = db + 1
    else: 
        print("Akkor nincs szökőév")
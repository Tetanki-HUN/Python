'''
Olyan függvény amely kiszámolja egy kúpnak a térfogatát 
r sugárból és m magasságból kiszámolja a kúp térfogatát
V = r^2 * Pi * M/3
'''

from cmath import pi

def terf(r: int, M: int) -> float:
    return r * r * pi * M / 3

r = input("Mekkora a kúp sugara?: ")
M = input("Milyen magas a kúp?: ")
print(terf(r,M))
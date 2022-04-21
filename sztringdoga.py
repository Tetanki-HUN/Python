from random import random


szoveg = "A számítógép-programozás (vagy egyszerűen programozás) egy vagy több absztrakt algoritmus megvalósítását jelenti egy bizonyos programozási nyelven."
'''
Hányadik karakter kötőjel
'''

print(szoveg.find("-"))

'''
A szöveg első karaktere betű
'''

print(szoveg.startswith("A"))

'''
Darabold fel a szöveget a szóközök mentén a szavak nevű változóba
'''

lista = szoveg.split(" ")
print(lista)

'''
Vágd le a felesleges szóközöket as szöveg végéről
'''

print(szoveg.rstrip())

'''
Paraméterként egy számot kap 
random annyi számos lista 
kiírat
'''

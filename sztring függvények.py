from calendar import month_abbr


mondat = "it is wednesday my dudes" 
'''
capitalie()): Első karakter nagybetűsíti 
'''

print(mondat.capitalize())

'''
swapcase(): A nagybetűkjet kicsivel a kicsiket nagybetűvel írja ki
'''

print(mondat.swapcase())

'''
title(): Minden szó első betűje nagy lesz
'''

print(mondat.title())

'''
startswith(): Igazat ad vissza ha, a megadott karakterekkel v. karakterekkel kezdődik
'''

print(mondat.startswith("it"))

'''
endswith(): Igazat ad vissza ha, a megadott karakterekkel v. karakterekkel végződik
'''

print(mondat.endswith("my"))

'''
index(): Megadott kifejezés kezdetének indexét adja
'''

print(mondat.index("is"))

'''
Ha nincs benne akkor HIBÁT AD!!!!!!!
'''

'''
print(mondat.index("tuesday")) <---- HIBA
'''

'''
rindex(): A megadott kifejezés utolsó előfordulásának indexét adja:
'''

print(mondat.rindex("e"))

'''
isalnum(): Igazat ad, ha a kifejezésben csak  számok és betűk vannak
'''

print(mondat.isalnum())

'''
isalpha(): Igazat ad, ha a kifejezésben csak betűk vannak
'''

print(mondat.isalpha())

'''
isnumeric(): Igazat ad, ha a sztringben minden karakter szám
'''

print(mondat.isnumeric())

'''
isspace(): Igazat ad, ha a kifejezésben minden üres
sorttörés: /n tabulátor: //t és szóköz között
'''
ures = "    "
print(mondat.isspace())
print(ures.isspace())

'''
islower(): Igazat ad, ha a kifejezésben minden karakter nagybetűs
'''

print(mondat.islower())

'''
isupper: (): Igazat ad, ha a kifejezésben minden kisbetű
'''

print(mondat.isupper())

'''
istittle(): Igazat ad, ha a kifejezésben minden szó nagy kezdőbetűs
'''

print(mondat.istitle())

'''
join(): Lista elemeket összefűz megadott elválasztó karakterekkel
'''

lista = ("Wednesday", "AHHHHHHHHHHHHHHHHHHHHH")
print(" ".join(lista))

'''
strip(): A szöveg elejéről és végéről levágja a szóközöket 
'''
banana = ("        your mom               ")
print(banana)
print(banana.strip())

'''
lstrip(): A szöveg elejéről levágja a szóközöket 
'''

print(banana)
print(banana.lstrip())

'''
rstrip(): A szöveg végéről levágja a szóközöket 
'''

print(banana)
print(banana.rstrip())

'''
split(): A szöveget feldarabolja a megadott karakterek mentén, és a darabokat tömbbe teszi 
'''

szoveg = "keszke-ló-kutya-béka"
lista = szoveg.split("-")
print(lista)

'''
rsplit(): A szöveget feldarabolja a megadott karakterek mentén, és a darabokat tömbbe teszi
(max paraméter nélkül a mint split()) 
'''

szoveg = "keszke-ló-kutya-béka"
lista = szoveg.rsplit("-")
print(lista)

'''
splitlines(): A szöveget feldarabolja a sortörés mentén, és a darabokat tömbbe teszi
'''

szoveg = "keszke/nló/nkutya/nbéka"
print(lista)
lista = szoveg.splitlines("-")
print(lista)
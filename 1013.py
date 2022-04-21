import random

kezd = int(input('Add meg a tartomány legkisebb számát: ')) #Megkérdezi a felhasználótól hogy melyik számok között randomizáljon egy számot
veg = int(input('Add meg a tartomány legnagyobb számát: '))
gondolt_szam = random.randint(kezd,veg)  #Random szám generálás
print('Súgok: ', gondolt_szam)
tipp = int(input('Gondoltam egy számra. Tippeld meg! '))
# ell: a tipp tartományon bellül van e
if tipp < kezd or tipp > veg:
    print('A tipped a megadott tartományon kívül van.')
while tipp != gondolt_szam:   #Addig kérjen tippeket amíg nem találja el a számot
   tipp = int(input('Nem talált próbáld újra! '))
   if tipp < kezd or tipp > veg:
    print('A tipped a megadott tartományon kívül van.')
print('Eltaláltad! :D')

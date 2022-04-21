myList = ["alma", "Barack", "Ananász", "Répa", "Körte"]
print(myList)

'''
Egymás alá írni listát.
'''
for i in range(len(myList)):
    print(myList[i])

'''
Listaelemek hosszának kiiratása
'''
for i in range(len(myList)):
    print(len(myList[i]))
    

'''
Irassuk ki azokat a szavakat amik az "A" betűvel kezdődnek
'''
for i in range(len(myList)):
    if myList[i][0] == "A":
        print(myList[i], end=" ")



'''
A kis és nagy betűket ne különböztesse meg + spaccel írja ki a listát
'''
for i in range(len(myList)):
    if myList[i][0].lower() == "a":
        print(myList[i],  end=" ")
        
'''
Egy szó kikeresése egy mondatból
'''    
mondat = "Ki szereti a rétest?"
print("rétest" in mondat)
    
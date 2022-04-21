#lista létrehozása
myList = ["Audi", "Peugeot", "Volswagen"]

#ellenőrzés
print(myList)

#listaelem elérése
print(myList[1])

#listaelemek száma
print(len(myList))

#a mindenkori utolsó kiiratása:
print(myList[len(myList)-1])

#elem beszúrása megadott helyre
myList.insert(2, "Suzuki")
print(myList)

#beszúrás a mindenkori utolsó helyre
myList.insert(len(myList), "Renault")
print(myList)

#listaelem eltávolítása
myList.pop(2)
print(myList)

#listaelem eltávolítása tartalom alapján
myList.remove("Pegueot")
print(myList)

#lista bejárása
for i in range(len(myList)):
    print(myList[i])

for i in range(len(myList)):
    if myList[i] == "Audi":
        print("Ez Audi")

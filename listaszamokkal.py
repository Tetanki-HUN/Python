#lista létrehozása és írj bele 10 számot
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList)

#Kérj be a felhasználótól egy számot, szúrd be a 2. helyre
szam = int(input("Mondj egy számot kérlerk: "))
myList.insert(1, szam)
print(myList)

#Rendezd sorba a listát
myList.sort()
print(myList)
a = input("Mondj nekem egy darab számot kérlek! ")
b = input("Mondanál kérlek egy másodikat? ")
c = input("Na ez az utolsó, kérlek mondj egy harmadik számot: ")

maximum = max(a,b,c)
minimum = min(a,b,c)
if (a != maximum and a != minimum):
    medium = a
elif (b != maximum and b != minimum):
    medium = b
else:
    medium = c

print(maximum, medium, minimum)





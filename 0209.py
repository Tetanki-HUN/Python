a = input("Mondj nekem egy darab számot kérlek! ")
b = input("Mondanál kérlek egy másodikat? ")
c = input("Na ez az utolsó, kérlek mondj egy harmadik számot")

if a > b and c and b > c:
    print("Szerintem" ,a, "nagyobb mint" ,b, "és," ,b, "nagyobb mint" ,c,)
elif b > a and c and a > c:
    print("Szerintem" ,b, "nagyobb mint" ,a, "és," ,a, "nagyobb mint" ,c,)
elif c > a and b and a > b:
    print("Szerintem" ,c, "nagyobb mint" ,a, "és," ,a, "nagyobb mint" ,b,)
elif c > a and b and b > a:
    print("Szerintem" ,c, "nagyobb mint" ,b, "és," ,b, "nagyobb mint" ,a,)
elif a > b and c and c > b:
    print("Szerintem" ,a, "nagyobb mint" ,c, "és" ,c, "nagyobb mint" ,b,)
elif b > a and c and c > a:
    print("Szerintem" ,b, "nagyobb mint" ,a, "és," ,c, "nagyobb mint" ,a,)
else:
    print("A három szám között van egyenlő vagy mindhárom egyenlő")
a = int(input('Mondj nekem egy egész számot: '))
b = int(input('Mondj nekem még egy darab egész számot: '))


if b == a:
    print("Szerintem a két szám egyenlő")
else:
    print("Szerintem " ,max(a,b), " nagyobb mint " ,min(a,b),)

import math

M = int(input('Mekkora a gúla magassága? '))
A = int(input('Mekkora a gúla alapjának élhossza? '))
at = pow(A,2)

if M > 0:
    mharomszog = math.sqrt((M*M)+pow(A/2,2))
    alapterulet = ((A*mharomszog)/2)
    print('A gúla alapterülete: ', at,)
    print('A gúla térfogata: ', ((at*M)/3),)
    print('Szabályos gúla oldallapjának területe', ((A*mharomszog)/2))
    print('Szabályos gúla felszíne: ', at+4*alapterulet,)    
    
else:
    print('Nem lehet kiszámolni.')
#Ha a gúla magassága nagyobb 0-nál akkor számolja ki a területét és a térfogatát.
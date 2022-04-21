'''
Bekéri a pontszámot
Értékelünk
00-39 1-es

40-54 2-es

55-69 3-as

70-84 4-es

85-100 5-ös
kiírja az értékelést
'''

A = int(input("Hány pontot értél el? "))

if 85 <= A:
    print("5-öst kaptál!")
elif A >= 70:
    print("4-est kaptál!")
elif A >= 55:
    print("3-ast kaptál!")
elif A >= 40:
    print("2-est kaptál!")
elif A >= 0:
 print("1-est kaptál!")

'''
Ugyanez csak ismételje addigamíg 1 db -1-est nem ad
'''

B = int(input("Hány pontot értél el? "))

while B != -1:
    if 85 <= B:
        print("5-öst kaptál!")
    elif B >= 70:
        print("4-est kaptál!")
    elif B >= 55:
        print("3-ast kaptál!")
    elif B >= 40:
        print("2-est kaptál!")
    elif B >= 0:
        print("1-est kaptál!")
    B = int(input("Hány pontot értél el? "))


'''
Számoljuk meg hány jeles dolgozat van
'''

B = int(input("Hány pontot értél el? "))
C = 0

while B != -1:
    print(C (" 5-ös van"))
    if 85 <= B:
        C = C + 1
        print("5-öst kaptál!")
    elif B >= 70:
        print("4-est kaptál!")
    elif B >= 55:
        print("3-ast kaptál!")
    elif B >= 40:
        print("2-est kaptál!")
    elif B >= 0:
        print("1-est kaptál!")
    B = int(input("Hány pontot értél el? "))
print(C, " 5-ös van.")


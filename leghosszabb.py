def mgh(nap: str) -> int:
    db: int = 0
    mgh = "aáeéiíoóöőuúüű"
    for i in range(len(nap)):
        if nap[i] in mgh:
            db += 1
    return db

napok =   ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek','szombat', 'vasárnap']


maxHely = 0

for i in range(len(napok)):
    if(mgh(napok[i]) > mgh(napok[maxHely])):
        maxHely = i
    
print("A legtöbb magánhangzót tartalmazó nap: ", napok[maxHely])
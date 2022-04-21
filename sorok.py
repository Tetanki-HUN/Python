sorok = []

file = open('kaja.txt', 'r', encoding='utf-8')
 
for e in file:
    sorok.append(e.strip())
    
print(sorok)

számok = []

file2 = open('szamok.txt', 'r', encoding='utf-8')
 
for e in file2:
    számok.append(e.strip())
print(számok)
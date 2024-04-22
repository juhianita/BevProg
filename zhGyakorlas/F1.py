#Juhász Anita Dóra C34WYZ

kicsi = int(input())
while True:
    try:
        szam = int(input())
        if szam < kicsi:
            kicsi = szam
        else:
            pass
    except EOFError:
        break
szorzat = 1
kicsi = str(kicsi)
for szamjegy in kicsi:
    szamjegy = int(szamjegy)
    szorzat *= szamjegy
print(szorzat)
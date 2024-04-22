#Juhász Anita Dóra C34WYZ

import random
n = int(input("n = "))
hetteloszthato = []
db = 0
for i in range(n):
    szam = random.randint(15,65)
    if szam % 7 == 0:
        hetteloszthato.append(szam)
        db += 1
    print(szam, end=" ")
if db == 0:
    print("\n0")
else:
    atlag = sum(hetteloszthato)/db
    print("\n"f"{(atlag):.2f}")

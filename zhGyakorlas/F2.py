#Juhász Anita Dóra C34WYZ

hetesekszama = 0
while True:
    n = input()
    if n == "STOP":
        break
    else:
        n = int(n)
        if n % 10 == 7:
            hetesekszama += 1
print(hetesekszama)


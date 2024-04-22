#Juhász Anita Dóra C34WYZ


ujszavak = []
while True:
    ujszo = ""
    szo = input()
    if szo == "END":
        break
    for betu in szo:
        if betu.lower() in "aáeéiíuúüűoóöő":
            ujszo += betu + "*"
        else:
            ujszo += betu
    ujszavak.append(ujszo)
for elem in ujszavak:
    print(elem)


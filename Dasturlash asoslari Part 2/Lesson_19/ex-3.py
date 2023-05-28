def oraliq(min, max):
    sonlar =[]
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar
print(oraliq(1,10))
print(oraliq(10,21))
print(oraliq(0,21, 2))

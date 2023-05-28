def oraliq(min, max):
    numbers = []
    while min<max:
        numbers.append(min)
        min += 1
    return numbers
print(oraliq(100,104))
print(max(oraliq(100,104)))
ask = int(input("what is number:\n>>>"))
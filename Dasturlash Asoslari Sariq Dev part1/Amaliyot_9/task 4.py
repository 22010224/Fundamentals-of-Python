menu = list(range(2,11))
number = int(input("Enter your number:>>>"))
devide =[]
for number in menu:
    if number/2 == 0:
        devide.append(menu)
        print(f"{number} is devided into {devide}")
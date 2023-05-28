# recovering mistakes

print("Hello World")
print("Let's count till 10")
for n in range(10):
    print(n+1, end=',')

number = 60
ask = int(input("Enter your number: \n>>>"))
gesture = True
while gesture:
    if number > ask:
        print(f" 60 > {ask}")
    elif number < ask:
        print(f"60<{ask}")
    else:
        print(f"{number}={ask}")

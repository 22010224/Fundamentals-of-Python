x = float(input("Enter your first number: \n>>>"))
y = float(input("Enter your second number: \n>>>"))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")
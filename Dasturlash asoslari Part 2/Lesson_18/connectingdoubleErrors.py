n = input("Enter integer number:\n>>>")
try:
    n = int(n)
    x = 20/n
except ValueError:
    print("Enter integer number:\n>>>")
except ZeroDivisionError:
    print("20 isn't divided by 0 ")
else:
    print(f"x={x}")
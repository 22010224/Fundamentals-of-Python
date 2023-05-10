rows = int(input("how many rows?"))
columms = int(input("how many columns"))
symbol = input("Enter your symbol")

for i in range(rows):
    for j in range(columms):
        print(symbol, end =" ")
        print()
print("Enter what you wanna purchase: ")
mahsulotlar =[]
products = input("Enter: ")
n = 1
while True:
    ask = f"Do you wanna buy again: (yes/no)"
    if ask == "yes":
        n+=1
    else:
        print("Done!")
    print("Process has been finished. Thanks! ")
    mahsulotlar.append(products)
    print(f"We accepted {mahsulotlar}")


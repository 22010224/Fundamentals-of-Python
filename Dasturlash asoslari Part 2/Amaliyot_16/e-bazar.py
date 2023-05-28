print("Enter what you wanna purchase: ")


gesture = True
while gesture:
    mahsulot = input("Enter what  you wanna buy : ")
    price = int(input("Enter the price of this product: "))
    javob = input("Again? (yes/no")
    if javob == 'yes':
        continue

       #     print(products)
mahsulotlar = {'olma','banan','behi'}
if products in mahsulotlar:
    print(f"We have {mahsulotlar}")
else:
    print(f"Sorry, we don't have this products: {mahsulot}")



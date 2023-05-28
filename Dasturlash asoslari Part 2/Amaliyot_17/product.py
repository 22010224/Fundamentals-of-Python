products = ['un','tuxum','gusht','piyoz','shakar','shkalad' ,'olam','banan','quyon','qovun','tarvuz']
savat =[]
for n in range(5):
    savat.append(input(f"{n+1}- mahsulotni kiriting: \>>>"))
    if savat:
        for product in savat:
            if product in products:
                print(f"There are {product} in our store!" )
            elif product not in products:
                print(f"Sorry, THERE are not {product} right now!")
            else:
                print("You haven't chosen anything, bro!")






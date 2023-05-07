products = ['apple','pineappple','book','tea','bread','bluthes','phone','laptop','flower','cup','dishes']
#print(len(products))
orders = ['apple','pineappple','book','tea','bread','bluthes','phone', 'honey']
for order in orders:
    if order in products:
        print(f"Your oder which is {order} has been excepted!")
    else:
        print(f"Sorry, We don't have '{order}'!")
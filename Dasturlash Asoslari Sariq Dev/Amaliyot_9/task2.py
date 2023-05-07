menu = ['apple','pineappple','book','tea','bread','bluthes','phone','laptop','flower','cup','dishes']
#print(len(products))
orders =[]
have = []
not_have = []
client = input("What do you wanna it?")
orders.append(client)
for  order in menu:
    if  order in menu:
        have.append(order)
        print(f"We have {have}")
    else:
        not_have.append(order)
        print(f"We don't have {not_have}")


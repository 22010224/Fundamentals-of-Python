menu = ['osh','manti','shashlik','norin','somsa']
order = input(("What do you wanna eat?>>>"))
if order.lower() in menu:
    print("Your order has been excepted")
else:

    print(f"sorry, we don't have {order} ")
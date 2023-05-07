menu = ['osh','manti','shashlik','norin','somsa']
order = ['osh','norin','somsa']
for meal in order:
    if meal in menu:
        print(f"Your these orders have been excepted: {meal }")
    else:
        print(f"Sorry, we don't have {meal} ")

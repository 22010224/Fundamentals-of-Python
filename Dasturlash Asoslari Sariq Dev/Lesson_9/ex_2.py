age = int(input("AGE?"))
    if age<= 4:
        price = "tekin"
    elif age <= 12:
        price = 5000
    elif age <= 10:
        price = 8000
    else:
        price = 10000
print(f"Siz uchun chipta  narxi {price}")


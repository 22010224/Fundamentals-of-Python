yosh = input("Enter age: \n>>>")
try:
    yosh = int(yosh)
    print(f"Siz {2023-yosh}-yilsiz !")
except:
    print("Enter integer, please!")
age = input("Enter your age: ")
try:
    age=int(age)
    print(f"You're born in {2023-age} year! ")
except:
    print("Enter integer number, please!")
print("Process has finished!")

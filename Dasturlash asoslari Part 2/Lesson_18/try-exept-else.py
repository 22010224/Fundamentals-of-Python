age = input("Enter your age: ")
try:
    age=int(age)

except:
    print("Didn't enter integer!")
else:
    print(f"You're born in {2023 - age} year! ")
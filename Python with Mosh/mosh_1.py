def get_user():
    print("Hi there")
    print("Welcome abroad")

    print("start")
    greet_user("John")
    print("Finish")


def square(number):
    return number**2
print(square(3))

try:
    age: int(input("Age:"))
    income = 20000
    print(income/age[0])
    print("Valuable")
except ValueError:
    print("Invalid Value")
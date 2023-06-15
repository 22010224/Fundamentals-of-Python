# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


temperature = 15
if temperature > 30:
    print( "It's warm")
    print("Drink more water!")
elif temperature >10:
    print("It's nice!")
else:
    print("Cold!")
print("DONE!...............................................")

# ->

age = 7
message = "Eligible"
if age >= 18:
    print(message)
else: print("Not Eligible")

# ->

numbers = (1,2,3)
print(numbers[0])
print(numbers[1])
print(numbers[2])

# ->

cordinates = (1,2,3)
x,y,z = cordinates
print(x+y+z)
print(x+y**z)


# ->
customer = {
    "name" : "John Smith",
    "age": 30,
    "is_verified":True

}
print(customer["name"])
print(customer.get['name'])
customer["birthday"]="October 23, 2004"
#
#
#
# ->



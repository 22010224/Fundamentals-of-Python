numbers = [1,2,3,4,5,6,7,8]
print(numbers[0])

cordinates = (1,2,3)
x,y,z = cordinates
print(x*y**z)

customer = {
    "name":"John Smith",
    "age": 18,
    "is_verified": True
}
print(customer["name"])
#print(customer.get["name"])
customer["birthday"] = "23, October"
print(customer["birthday"])

phone =int(input("Phone:"))
digit_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output = " "
for ch in phone:
    output+=digit_mapping.get(ch, "!" + " ")
print(output)
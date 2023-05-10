#2d lists -> a list of lists

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","osh"]
dessert = ["cake","ice-cream"]
food = [drinks,dinner,dessert]
print(food[1][2])

#tuple -> collection which is ordered

student = ("Saxa", 18, "male")
print(student.count("Saxa"))
print(student.index("male"))
for x in student:
    print(x, end = " ")
    if "Saxa" in student:
        print("Saxa is here!")

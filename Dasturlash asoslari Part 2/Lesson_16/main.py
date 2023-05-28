names = []
print("Let's create the list of your close friends ")
n = 1
while True:
    question = f"{n}- enter the name of your friend : "
    name = input(question)
    names.append(name)
    answer = input("Do you add name again? (ha/Yo'q) ")
    if answer=='Ha':
        n+=1
        continue
    else:
        break
        print("Done!")
print("List has been created, Thanks")
print("Names of friends : ")
for name in names:
    print(name.title())
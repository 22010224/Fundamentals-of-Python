print("Let's keep the age of your friends:  ")
friends = []
gesture = True
while gesture:
    name = input("Enter your friend's name : ")
    age = int(input("Enter the age of your friend: "))
    friends[name] = int(age)

    answer = input("Do you wanna add somthing else? (yes/no) " )
    if answer=="no":
        gesture = False
        print("Done!")
    else:
        gesture = True

    print(friends)
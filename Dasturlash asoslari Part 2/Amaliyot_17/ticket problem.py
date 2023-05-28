age = int(input("How old are you?\n>>>"))
if age <= 4 or age >=65:
    print(f"Ticket is free for the citizen who is at the age of {age}. Congratulations!🎉🎉🎉")
elif age<18:
    print("5000 uzs")
else:
    print("8000 uzs")
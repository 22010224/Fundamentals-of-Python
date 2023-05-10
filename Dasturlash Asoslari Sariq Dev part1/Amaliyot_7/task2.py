meetings =[]
print("How many people you had a conversation today?")
for n in range(4):
    meetings.append(input(f"Enter your {n+1}th partner,please:"))
    print(meetings)
    print(len(meetings))
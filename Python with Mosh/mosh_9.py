for i in range(1,23):
    if i == 13:
        pass
    else:
        print(i)


food = ["osh","shurva","manti"]
food[0] = "palov"
food.append("hot dog")
food.append("ice-cream")
food.remove("hot dog")
food.sort()
food.insert(0, "cake")
food.pop(-1)
food.clear()
for x in food:
    print(x)
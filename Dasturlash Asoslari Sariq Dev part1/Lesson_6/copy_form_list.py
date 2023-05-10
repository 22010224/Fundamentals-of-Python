numbers = [1,2,3,4,5,6]
numbers2 = numbers
numbers2.append(8)
numbers2.append(7)
print(numbers)
print(numbers2)

numbers2 = numbers[:]
numbers2.append(8)
numbers2.append(7)
print("This is the list of numbers:",numbers)
print("This is the list of numbers2:",numbers2)


numbers = {1,2,3,4,5,6,7,87,8,8,89,8,8}
print(len(set(numbers)))
a = set()
#print(numbers[2])
fruits = ['apple','pineapple','peach','apple','apple','apple']
fruits = set(fruits)
print(fruits)
#fruits = list(fruits)
#print(list(fruits))
fruits.add('banana')
print(fruits)
fruits.update(['anor','melon'])
print(fruits)

fruits.discard('banana')
fruits.remove('apple')
print(fruits)
number = numbers.pop()
print(number)
print(numbers)

A = {1,2,3,4}
B = {3,4,5,6}
C = A|B # -> Union of sets
C1 = A&B # -> Intersection of sets
print(C)
print(C1)
print(A-B)
print(B-A)
print(A^B)
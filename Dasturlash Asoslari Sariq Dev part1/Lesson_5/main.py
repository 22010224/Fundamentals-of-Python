fruits = ['apple','anjir','shaftoli','apricot','peach']
print("The first fruits : "+fruits[0])
print(f"The second friut : " + fruits[1])

print("The first fruits : "+fruits[0].title().upper())
print(f"The second friut : " + fruits[1].upper())

prices = [120000,18000,302908,23998293893]
print((prices[0]+prices[3])**2)
numbers = [120000,18000,302908,23998293893,31124132,124142143,23575585,679989,653,53,533434,0,43534543]
print(numbers[-1])
print(numbers[-2])

fruits.append("melon")
print(fruits)

prices[0]=130000
print(prices[0])


cars =[]
cars.append("Lacetti")

cars.append("Malibu")
cars.append("Bugatti")
cars.append("Rolls-Royce")


cars.insert(0,'Lamborghini 2021')

cars.insert(2,'Matiz')
print(cars)


del cars[1]
print(cars)
#fruits.remove[1]
#fruits.remove('apple')
print(fruits)

bozorlik = ["oil",'flour', 'onion', 'banana','meat']
product = bozorlik.pop(3)
print(f"I bought {product}")
print("Unbought products: ", bozorlik)
product1 = bozorlik.pop()
print(product1, bozorlik)


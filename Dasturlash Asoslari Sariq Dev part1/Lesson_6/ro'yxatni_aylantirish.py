fruits =['pear','apple','banana','melon','watermelon']
fruits.reverse()
print(fruits)

print("The numbers of elaments:",len(fruits))
numbers = list(range(0,10))
print(numbers)

even_numbers = list(range(0,100,2))
odd_numbers = list(range(1,100,2))
print("Juft sonlar:", even_numbers)
print("Toq sonlar:",odd_numbers)

prices = [ 12000, 13000,140000,21000,32000000, 12100,42000]
cheap = min(prices)
expensive = max(prices)
overall = sum(prices)
print("The cheapest tool's price:",cheap,"so'm",\
      ". The most expensive one: ", expensive,"so'm",\
      ". Overall:", overall,"so'm")

my_tools = prices[0:3]
print(my_tools)
print(fruits[2:4])
print(fruits[:4])
print(prices[2:])

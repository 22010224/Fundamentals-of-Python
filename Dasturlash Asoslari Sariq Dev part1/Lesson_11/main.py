student = {'name':'Samandar',
           'age':18,
           'university':'IDU',
           'faculty':'Computer Science'}
print(student.items())
for key, variable in student.items():
    print(f" Key: {key},\n Variable: {variable}")

phones = {'ali':'iphone 14 pro max',
          'vali':'iphone x',
          'hasan':'red mi pro max',
          'husan':'samsung galay pro max'}
for x, y in phones.items() :
    print(f"{x.title()}ning telefoni {y.upper()}")



products = {
    'apple':10000,
    'pineapple':200000,
    'grapes': 3000,
    'peach':42000,
    'pear':3200,
    'apple':10000,
    'pineapple':200000,
    'grapes': 3000,
    'peach':42000,
    'pear':3200
}
print(products.keys())
for product in products.keys():
    print(product.title())
for product in products.keys():
    if product in products:
        print(f"{product.title()} {products[product]}uzs")
print("Bizadagi products:")
for product in sorted(products):
    print(product.title())
print(products.values())
print("Prices:")
for product in products.values():
    print(f"{product} uzs")
print(products)
for product in sorted(products.values()):
    print(product)



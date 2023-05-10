price = 15000
tea = True
salat = False
non = True
kompot = True
assorti = False

if tea:
    print("Client got tea")
    price = price + 5000
if salat:
    print("CLient got salat")
    price = price + 10000
if non:
    print("CLient got non")
    price = price +7000
if kompot:
    print("Client got kompot")
    price = price + 15000
if assorti:
    print("Client got assorti")
    price =price + 20000
print(f"Overall: { price}")
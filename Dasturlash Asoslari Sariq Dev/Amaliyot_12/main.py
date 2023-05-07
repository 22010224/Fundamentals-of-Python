colors = {'red','green','blue'}
colors.add('black')
print(colors)
colors.update('orange','yellow')

set1 ={10,20,30,40,50}
set2 ={30,40,50,60,70}
# -> union
print(set1|set2)
# -> intersection
print(set1&set2)
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

bozorlik = {'choy','non','kartoshka','tuxum','sut'}
mahsulotlar = {'non','sut','tuxum','olma','un','tuz'}
have = {}
have = (bozorlik&mahsulotlar)
havenot = {}
havenot = (bozorlik-mahsulotlar)
print(f"We cannot buy these products: {havenot}")
print(f"We can purchase : {have} ")
mahsulotlar.update(['gusht','piyoz','anjir'])
print(mahsulotlar)
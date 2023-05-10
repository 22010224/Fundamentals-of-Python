car0 = {'model':'lacetti',
        'color':'white',
        'year': 2018,
        'price': 13000
        }
car1 = {'model':'gentra',
        'color':'red',
        'year': 2018,
        'price': 12000
        }
car2 = {'model':'malibu',
        'color':'black',
        'year': 2018,
        'price': 23000
        }
cars = [car0,car1,car2]
print(cars)
for car in cars:
    print(f"{car['model'].title()}, "
          f"rangi {car['color']},"
          f"yili {car['year']},"
          f"narxi {car['price']}")

print(cars[0])
print(cars[0] ['model'])
print(f"{cars[2] ['color'].title()} "
      f"{cars[2] ['model'].title()}")

malibus = []
for n in range(13):
    new_car = {
        'model': 'kaptiva',
        'color': 'white',
        'year': 2015,
        'price': 19000,
        'karobka': 'avto'

    }
    malibus.append(new_car)
    for malibu in malibus:
        print(malibu.values()


# Lug'at ichida ro'yxat
coders = {
    'ali': ['python','C++'],
    'vali':['html','css','javascript'],
    'hasan':['php','sql'],
    'husan':['python']
    }
        for names, languages in coders.items():
            print(f"\n{names.titles():}", end='')
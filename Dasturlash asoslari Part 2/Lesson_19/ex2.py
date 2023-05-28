def avto_info(make,model, rangi, karobka, yili,narxi=None):
    avto = {'kompoaniya':make,
            'model':model,
            'rang':rangi,
            'korobka':karobka,
            'yil':yili,
            'marx':narxi}
    return avto
avto1 = avto_info('GM','Malibu','Qora','Avtomat', 2018)
avto2 = avto_info('GM','Nexia 3', 'oq', 'Mexanika',2016,15000)
avtolar = [avto1,avto2]
print("Online bozorda mavjud bo'lgan mashinalar: ")
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else:
        narx = "Noma'lum"
    print(f"{avto['rang']}{avto['model']}. Narxi: {narx}")
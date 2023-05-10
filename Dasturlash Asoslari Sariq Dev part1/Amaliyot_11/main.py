python = {'set':'settings',
          'variables': 'abc',
          'loops':'while',
          'cycles': 'sikls',
          'print' :'printing'
}
print(sorted(python.values()))


coubtries = {'USA':'Washington',
             'Uzbekistan': 'Tashkent',
             'Germany':'Berlin',
             'Britain':'London',
             'Canada':'Ottawa',
             'Italy':'Roma'}
print(f"Davlatlar : {sorted(coubtries.keys())}")
print(f"Poytaxtlar: {sorted(coubtries.values())}")
ask = input("Choose a country: ")
for x in coubtries.keys():
    if x in coubtries:
        print(f"The capital of {x} is {coubtries.get(x)}")
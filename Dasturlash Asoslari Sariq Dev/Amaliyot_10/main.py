family = {'otam':'Mansurjon',
          'onam':'Gulyoraxon',
          'ukam':'Fayzulloh'}
print(family)
print(f" Otajonimning ismlari {family.get('otam').upper()},\n Onajonimning ismlari {family.get('onam').upper()},\n Ukamning ismi {family.get('ukam').title()}")

meals = {'number1':'osh',
         'number2':'shurva',
         'number3':'manti',
         'number4':'somsa',
         'number5':'chuchvara'}
print(f"{family.get('otam').title()}ning eng sevimli taomi {meals.get('number1').title()}")


ask = (input("Search?>>>"))

if n in meals:
    print(f"We have ")
else:
    print(f"We don't have {n}")

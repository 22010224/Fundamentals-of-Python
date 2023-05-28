fruits = ['apple','peach','apricot','grapes','behi']
try:
    print(fruits[7])
except IndexError:
    print(f"There isn't 7th element in this list, nro! We have only {len(fruits)} fruits here")
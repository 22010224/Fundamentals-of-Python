countries =['USA','Uzbekistan','Germany','Africa']
print(len(countries))
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
countries.sort(reverse=False)
print(countries)
print(countries)
numbers = list(range(120, 1200,2))
print("Even numbers:", numbers)
print(sum(numbers))
print(max(numbers) - min(numbers))
print(len(numbers))
print(numbers[:20])
print(len(numbers[520:]))
print(numbers[260:280])


meals = ['osh','manti','chuchvara','shurva','gulkaram']
nonushta = meals[:]
nonushta.append('palov')
nonushta.append('karam')
nonushta.remove('manti')
print(nonushta)
print(meals)
nonushta = tuple(nonushta)
nonushta = list(nonushta)
nonushta[0]="qaymoq va non"
print(nonushta)
tomonlar = (20,30,60.2)
print(tomonlar)

toys = ('bus','bear',',car','dino','snake','lizard')
print(toys[0])
print(toys[2:])
print(toys[2:4])

toys = list(toys) # (list)
toys.append('dragon')
toys.remove('bear')
del toys[-1]
toys[1]='mcqueen'
print(toys)
toys=tuple(toys)
print(toys)
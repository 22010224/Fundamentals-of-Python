son = 1
while son<=5:
    print(son, end=' ')
    son = son+1
breakpoint()
print("Kiritinlgan sonning kvadratinin qaytaruvchi dastur:")
savol = "Istalgan son kiriting"
savol += "(To'xtatish uchun 'exit' deb yozing):"
value = ''
while value != 'exit':
    value = input(savol)
    if value != 'exit':
        print(float(value)**2)

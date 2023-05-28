print("Kiritinlgan sonning kvadratini qaytaruvchi dastur: ")
question = "Istalgan son kirting:"
question += "(to'xtatish uchun 'exit' deb yozing): "
gesture = True
while gesture:
    value = input(question)
    if value == 'exit':
        gesture = False
    else:
        print(float(value)**2)
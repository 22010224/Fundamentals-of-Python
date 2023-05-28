print("saytimizning avtolar royxatinin shaklantiramiz.")
avtolar = []
while True:
    print("\nQuyidagi ma'limotlarni kiriting", end='')
    kompaniya = input("Ishlab chiqaruvchi:")
    model = input("Modeli: ")
    rangi = input('rangi:')
    yili = input("Karobka: ")
    narx = input("Narxi: ")
    avtolar.append(avto_info(kompaniya,model,rangi, yili,narx))
    javob = input("Yana avto qushasimi? yes/no \n>>>")
    if javob=='no':
        break
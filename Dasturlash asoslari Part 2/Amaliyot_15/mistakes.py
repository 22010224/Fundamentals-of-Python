savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n>>> "
savol += "Enter an even number"
savol += "(write 'quit' to stop the programm:)"
while True:
    value = int(input(savol))
    if value <0:
        continue
    elif value == 'quit':
        break
    else:
        ildiz = float(value)**(0.5)
        print(f"{value} ning ildizi {ildiz} ga teng ")
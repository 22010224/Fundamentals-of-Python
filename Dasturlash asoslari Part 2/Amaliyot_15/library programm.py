print("let's write a code for bus stations: ")
ask = int(input("Yoshingizni kiriting:"))
ask +=int(input( "(dasturni tugatish uchun 'quit' deb yozing):"))
ishora = True
while ishora:
    value = ask

    if ask <= 7:
        print("2000 uzs")
    elif ask <= 18:
        print("3000 uzs")
    elif ask < 65:
        print("10000 uzs")
    elif value == 'quit':
        ishora =False
        print("Thanks, progress has been finished")
    else:
        print("Free for olders! Thanks")




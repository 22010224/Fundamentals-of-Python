print("Istagan kitobingizni topishga yordamlashamiz: : ")
ask = "Istalgan kitobingizning nomini kiriting: "
ask+="(dastur to'xtashi uchun 'stop' deb yozing):"
gesture = True
while gesture:
    value = input(ask)
    if value == 'stop':
        gesture=False
        print("Done! progress has been finished!")
    else:
        print(f"Do you like {value} book? LOL :)")
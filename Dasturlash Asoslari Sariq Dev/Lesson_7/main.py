mehmonlar = ['ALi','Hasan','Husan','Olim','Obid']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni kelayotgan shanba kuni nahorgi oshga taklif qilamiz!")
    print("Done!")
print("Dastur tugadi!")

cars = ['nexia','tico','damas']
for car in cars:
    print(car.title(), " mashinasi")
    print("Ko'rganlar havas qilar!")

numbers = list(range(1,11))
for son in numbers:
    print(f"{son} ning kvadrati {son**2}ga teng")
number =list(range(11))
son_kvadrati = []
for son in number:
    son_kvadrati.append(son**2)
print(number)
print(son_kvadrati)


friends = []
print("Enter your 5 friends:")
for n in range(5):
    friends.append(input(f"{n+1}- do'stingizning ismi:\>>>"))
    print(friends)
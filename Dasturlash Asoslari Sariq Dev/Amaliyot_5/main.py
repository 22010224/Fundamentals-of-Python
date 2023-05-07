names = ["Ali","Hasan","Husan"]
print("Hi", names[0])
print(names[1] + " va " +names[2] +" egizaklar")
print(names.pop(2) + " loves his brother")



numbers = [28768743,258781,-871874587, 8734872582]
print(numbers[0]*numbers[-1]  +numbers[2]*numbers[1])

t_people =[]
z_people = []
t_people.append("Imom Buxoriy")
print(t_people)
z_people.append("Elon Mask")
print(z_people)
z_people.append("Bill Gates")
print(f" I know {t_people.pop(0) }  as a historical great scientist in Islam, and {z_people.pop(0)} as a modern billionarie")

guests = []
guests.append("Samandar")
guests.append("Ali")
guests.append("Hasan")
guests.append("Husan")

print(guests)
x = guests.remove("Hasan")
print(guests)
print(x)
guests.insert(0,"Abduraxmon")
guests.insert(2,"Sardor")
guests.insert(5, "John")
print(guests)
new_guest = guests.pop(0)
print(new_guest)
#new_guest.append("Abdurahim")
print(new_guest)
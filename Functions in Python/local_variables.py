def tuliq_ism_yasa(name, surname):
    """To'liq ism-familiyani qaytaruvchi funksiya"""
    tuliq_ism = f"{name.title()} {surname.title()}"
    return tuliq_ism


student1 = tuliq_ism_yasa('samandarbek', 'muqumov')
student2 = tuliq_ism_yasa('bahodir', 'jalolov')
print(f"Darsga kelmagan studentlar:  {student2.title()} va {student1.title()}")
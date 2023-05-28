def toliq_ism_yasa(ism, familiya, otasining_ismi = " "):
    """toliq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism}{familiya}"
    return toliq_ism.title()
student1 = toliq_ism_yasa('olim ','hakimov')
student2 = toliq_ism_yasa('saxa ','john')
print(f"Darsga kelmagan talabalar: {student1.title()} va {student2.title()}")
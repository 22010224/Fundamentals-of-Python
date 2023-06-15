def  toliq_ism_yasa(name,surname, otasining_ismi=''):
    """To'liq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{name} {surname}  {otasining_ismi}"
    else:
        toliq_ism = f"{name} {surname}"
        return toliq_ism.title()


    student1 = toliq_ism_yasa('olimov','shuxrat')
    student2 = toliq_ism_yasa('samandarbek','muqumov', 'mansurjonovich')
    print(f"Grand yutgan studentlar: {student2.title()} va {student1.title()}")




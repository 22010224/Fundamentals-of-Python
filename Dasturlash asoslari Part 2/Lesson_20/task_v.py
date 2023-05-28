def toliq_ism_yasa(ism, familiya, otasining_ismi=' '):
    if otasining_ismi:
        toliq_ism = "{ism} {familiya} {otasining_ismi}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism
studnet1 = toliq_ism_yasa("olim", "hakimov")
studnet2 = toliq_ism_yasa("olim","hakimov","botirovich")
print(f"Darsga kechikib kelgan talabalar: {studnet1.title()} va {studnet2.title()}")
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"{ism.title()}ning bahosini kiriting:\n>>>")
        baholar[ism]=baho
        return baholar
    students = ['ali','vali','hasan','husan']
    baholar = bahola(students[:])
    print(baholar)
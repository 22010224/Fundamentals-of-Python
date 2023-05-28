print("kvadtarni hisoblovchi dastur:")
savol = "Istalgan sonni kiriting"
savol += " To'xtatish uchun 'exit' deb yozing :)"
while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        print("Done! progress has been finished :)")
        break
    else:
        print(float(qiymat)**2)

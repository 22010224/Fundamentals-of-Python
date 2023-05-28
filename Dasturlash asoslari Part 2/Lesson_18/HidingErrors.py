user = {"username": "sariwdev",
        "status":"admin",
        "email":"admin@sariqdev.com",
        "phone":"+998950430479"}
key = "tel"
try:
        print(f'Foydalanuvchi:{user[key]}')
except KeyError:
    pass

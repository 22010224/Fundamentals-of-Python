while True:
    yosh = input("Enter your age:\n>>>")
    if yosh.isdigit():
        yosh = int(yosh)
        break

print(f"You're born in {2023-yosh}")

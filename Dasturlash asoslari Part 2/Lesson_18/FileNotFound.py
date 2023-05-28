file = "data.txt"
try:
    f = open(file)
except FileNotFoundError:
    print(f"{file} couldn't be found!")
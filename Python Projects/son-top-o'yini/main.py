import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Man 1 dan {x} gacha son o'yladim, topa olasizmi?", end=" ")
    while True:
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print(f"{taxmin} dan kattaroq son ayting:", end="")
        elif taxmin>tasodifiy_son:
            print(f"{taxmin}dan kichikroq son ayting:", end="")
        else:
            print("You WON! Congratulatioins👏🏻👏🏻👏🏻")
            break
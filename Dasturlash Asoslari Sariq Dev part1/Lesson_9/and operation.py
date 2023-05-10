day = input("What day is today?>>>")
degree_wheather = float(input("How much hot today?>>>"))
if day.lower() == 'sunday' and degree_wheather >= 30:
    print('Let\'s go to swimming🤪')
elif day.lower()=='sunday' and  degree_wheather<30:
    print("Stay home and do your hometasks! OK?")
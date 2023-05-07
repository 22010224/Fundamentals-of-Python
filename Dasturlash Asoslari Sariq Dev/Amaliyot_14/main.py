people = {
    'munisa_rizayeva':{
        'kasb':'artist',
        'money':'lot',
        'malumot':'oliy'
    },
    'laziz_ahmedov':{
        'kasb':'coder' ,
        'money':'lot',
        'malumot':'oliy'
    },
    'Samandar':
        {
            'kasb':'student',
            'money':'lot',
            'malumot':'oliy'
        },
    'Abduraxmon':{
            'kasb':'student',
            'money':'lot',
            'malumot':'oliy'
    }
}
people = list(people)
for names, info in people.items():
    print(f"\n{names.title}: {info.title()}")
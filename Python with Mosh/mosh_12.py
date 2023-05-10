# dictionary -> a changable, unordered collection of unique key value

capitals = {"USA": 'Washinton',
            "India":' New Dehli',
            "Russia": 'Mascow'
            }
capitals.update({"Germany":'Berlin'})
capitals.update({"USA":'Los Angles'})
capitals.pop("Russia")
capitals.clear()
#print(capitals["India"])
#print(capitals.key())
print(capitals.values())
print(capitals.items())
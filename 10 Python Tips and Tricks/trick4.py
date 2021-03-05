
"""
names = ["Peter Parker","Clark Kent","Wade Wilson","Bruce Wayne"]
heros = ["Spiderman","Superman","Deadpool","Batmen"]

for index,name in enumerate(names):
    hero = heros[index]
    print(f'{name} is actually {hero}')   """

names = ["Peter Parker","Clark Kent","Wade Wilson","Bruce Wayne"]
heroes = ["Spiderman","Superman","Deadpool","Batmen"]
universes = ["Marvel","DC","Marvel","Dc"]

for name,hero,universe in zip(names,heroes,universes):
    print(f'{name} is actually {hero} from {universe}')

for value in zip(names,heroes,universes):
    print(value)
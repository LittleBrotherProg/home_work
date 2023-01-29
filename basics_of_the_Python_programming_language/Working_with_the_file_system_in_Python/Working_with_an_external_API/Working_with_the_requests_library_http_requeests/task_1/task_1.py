import requests
url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
hero_int = {}
count_hero = int(input("Введите количество героев дял сравнения парматера intelligence" "\n"))
name_heros = []
def get_key(name_int, value_int):
    for key, value in name_int.items():
        if value == value_int:
            return key
for count in range(count_hero):
    name_heros.append(input(f"Введите {count_hero} имя Героя" "\n").capitalize())
for heros in resp.json():
    for name_hero in name_heros:
         if heros.get("name") == name_hero:
             hero_int[name_hero] = heros.get("powerstats").get("intelligence")

print("Самый большой показатель intelligence у",get_key(hero_int ,max(hero_int.values())))
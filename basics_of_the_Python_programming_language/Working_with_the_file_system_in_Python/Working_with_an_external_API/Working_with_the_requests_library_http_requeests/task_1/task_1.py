import requests
url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
hero_int = {}
count_hero = int(input("Введите количество героев дял сравнения парматера intelligence" "\n"))
name_heros = []
for count in range(count_hero):
    name_heros.append(input(f"Введите {count + 1} имя Героя" "\n").title())
for heros in resp.json():
    for name_hero in name_heros:
         if heros.get("name") == name_hero:
             hero_int[name_hero] = heros.get("powerstats").get("intelligence")

print("Самый большой показатель intelligence у", max(hero_int))
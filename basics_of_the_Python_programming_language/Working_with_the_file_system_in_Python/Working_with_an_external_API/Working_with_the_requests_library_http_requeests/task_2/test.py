import requests
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'y0_AgAAAAA8KgLcAADLWwAAAADa_KQ7iNJyZXM9TYq8pBI5cqN6ShBQyeU'
}
save = 'lol/8112.jpg'
url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
params = {"path": save, "overwrite": "false"}
result = requests.get(url, headers=headers, params = params)
result = requests.put((result.json()).get('href'), data=open('8112.jpg', 'rb'))

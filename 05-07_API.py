import requests
import json

ans = dict()
client_id = 'c98a26e74171f1d73c50'
client_secret = '6c2512c7f6c30c2e2c0251a33278b678'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

with open ('dataset_24476_4.txt', 'r', encoding='utf-8') as r:
    lst = r.readlines()

for i in lst:
    url = "https://api.artsy.net/api/artists/"+ i.rstrip()  # i == artist
    r = requests.get(url, headers=headers)
    j = json.loads(r.content.decode('utf-8'))
    ans[j['sortable_name']] = j['birthday']

fin = sorted(ans.items(), key = lambda x: (x[1], x[0]))

with open('res.txt', 'w', encoding= 'utf-8') as f:
    for k in fin:
        print(k[0])
        f.write(k[0]+ "\n")

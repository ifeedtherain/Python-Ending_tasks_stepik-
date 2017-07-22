import requests
import zipfile
import io
import json

mliquid = dict()

url = 'http://moex.com/iss/downloads/statistics/engines/stock/monthly/latest.json.zip' # необходимо в JSON добавить в конец ] к ]}
res = requests.get(url)

z = zipfile.ZipFile(io.BytesIO(res.content))
z.extractall()
z.close()

with io.open('monthly_archive.json', 'r', encoding='utf-8')as f:
    data_fl = json.load(f)
for i in range(len(data_fl['monthly']["data"])):
    if data_fl['monthly']["data"][i][8] >= 100000000000:
        mliquid[data_fl['monthly']["data"][i][5]] = data_fl['monthly']["data"][i][8]
print(mliquid)


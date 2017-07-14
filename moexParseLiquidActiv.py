import requests
import zipfile
import io
import json

mliquid = dict()

# url = 'http://moex.com/iss/downloads/statistics/engines/stock/monthly/latest.json.zip'
# res = requests.get(url)
#
# z = zipfile.ZipFile(io.BytesIO(res.content))
# z.extractall()
# z.close()

with io.open('monthly_archive.json', 'r', encoding='utf-8')as f:
    dataf = json.load(f)
# if dataf[8]>= 1000000:
#     mliquid[dataf[4]] += dataf[8]
print(mliquid)
print(dataf[2][6])

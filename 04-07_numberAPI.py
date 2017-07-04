import requests
number =[]
ans = []
url = 'http://numbersapi.com/'

with open('dataset_24476_3.txt', 'r') as f:
    row = f.readlines()
    for i in row:
        print(i)
        number.append(i.rstrip())

print(number)



for i in  number:
    try:
        url_new = url + i + '/math?json=true'
        print(url_new)

        res = requests.get(url_new)
        data = res.json()
        # print(data)
        if data['found'] == True:
            ans.append('Interesting')
        else:
            ans.append('Boring')
    except:
        pass

for i in ans:
    print(i)


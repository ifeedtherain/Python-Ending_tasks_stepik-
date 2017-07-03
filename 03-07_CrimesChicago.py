import csv

ans = dict()
with open('Crimes.csv') as f:
    data = csv.DictReader(f)
    for row in data:
        if(row['Date'][6:10]) == '2005':
            if row['Primary Type'] not in ans.keys():
                ans[row['Primary Type']] = 1
            elif row['Primary Type'] in ans.keys():
                ans[row['Primary Type']] += 1
for k, v in ans.items():
    if k == max(ans, key= ans.get):
        print(k,v)

x = []
h = []
temp = []
new = []
ans = []
for i in range(int(input())):
	x.append(input().lower())
for g in range(int(input())):
	h.append(input().lower())
for m in h:
	row = m.split(' ')
	temp.append(row)
for i in temp:
	for k in i:
		new.append(k)
for i in new:
	if i not in x:
		ans.append(i)
for i in set(ans):
	print(i)


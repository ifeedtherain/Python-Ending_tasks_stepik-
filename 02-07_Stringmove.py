s = str(input())
a = str(input())
b = str(input())
count = 0
mark = 0

while a in s:
	if a not in s:
		break
	if a in b:
		mark = 1
		print('Impossible')
		break
	s = s.replace(a,b)
	count += 1
if mark == 0:
	print(count)

x = [input().lower().split() for i in range(int(input()))]
x_temp, y_temp = 0, 0
for i in x:
	if i[0] == 'север':
		y_temp += int(i[1])
	if i[0] == 'запад':
		x_temp -= int(i[1])
	if i[0] == 'юг':
		y_temp -= int(i[1])
	if i[0] == 'восток':
		x_temp += int(i[1])

xy = [x_temp, y_temp]
print(*xy)
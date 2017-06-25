import re
ans = []
add = ''
f = open('dataset_3363_2.txt', 'r')
read_f = f.read()
reg = re.findall(r"(([a-zA-Z]+)([0-9]+))", str(read_f))
for i in reg:
	add += (str(i[1]) * int(i[2]))
print(add)


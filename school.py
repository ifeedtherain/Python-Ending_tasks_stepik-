file = open('dataset_3363_4.txt', 'r')
read_f = file.read().split('\n')
ans = []
for i in read_f:
	ans.append(i.split(';'))
print(read_f)
avg_math = []
avg_physc = []
avg_rus = []
for i in ans:
	try:
		print((int(i[1]) + int(i[2]) + int(i[3])) / 3)
		avg_math.append(int(i[1]))
		avg_physc.append(int(i[2]))
		avg_rus.append(int(i[3]))
	except IndexError:
		pass

print((sum(avg_math)/len(avg_math)), (sum(avg_physc)/len(avg_physc)), (sum(avg_rus)/len(avg_rus)))

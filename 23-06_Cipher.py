
def inv_dict(d):
	inv = dict()
	for k, v in d.items():
		inv[v] = k
	return inv

fb = ','.join(str(i) for i in input())  # input liter equals encoding to cb
cb = ','.join(str(i) for i in input())  # code cipher for fb
work_fb = ','.join(str(i) for i in input())  # encode
work_cb = ','.join(str(i) for i in input())  # decode
temp = []
work_fb_ans = []
work_cb_ans = []

for i in range(len(fb)):
	if i % 2 == 0:
		temp.append((fb[i], cb[i]))
d = dict(temp)
temp.clear()
s = inv_dict(d)

for i in work_fb:
	work_fb_ans.append(d.get(i))
for g in work_fb_ans:
	if g != None:
		temp.append(g)
work_fb_ans = [''.join(str(i) for i in temp)]
temp.clear()

for k in work_cb:
	work_cb_ans.append(s.get(k))
for x in work_cb_ans:
	if x != None:
		temp.append(x)
work_cb_ans = [''.join(str(i) for i in temp)]


print(*work_fb_ans)
print(*work_cb_ans)


"""
 Sample Input 1:

abcd
*d%#
abacabadaba
#*%*d*%

Sample Output 1:

*d*%*d*#*d*
dacabac

Sample Input 2:

dcba
badc
dcba
badc

Sample Output 2:

badc
dcba
"""
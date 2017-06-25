import collections
c = collections.Counter()
inp = open('dataset_3363_3.txt', 'r')
read_inp = inp.read().lower().split()
for i in read_inp:
	c[i] += 1
ans = tuple(*(c.most_common(1)))
print(*ans)

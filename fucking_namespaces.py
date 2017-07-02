dikt = dict()

def add(n, v):
	if n in dikt :
		dikt[n].append(v)

	else:
		dikt[n]= [v]
def create(n, p):
	for k,v in dikt.items():
		if k == p:

			dikt[k].append(n)
def get(n, p):
	for k, v in dikt.items():
		if (n, p) == (k, [v]):
			if k == p:
				print(k)
				return k


def find_path(dikt, start, end, path= []):
	path = path + [start]

	if start == end:
		return path

	if start not in dikt.keys():
		return None

	for node in dikt[start]:

		if node not in path:

			newpath = find_path(dikt, node, end, path)

			if newpath: return newpath

	return None

add('global', 'a')
create('foo', 'global')
add('foo', 'b')
get('foo', 'a')
get('foo', 'c')
create('bar', 'foo')
add('bar', 'a')
get('bar', 'a')
get('bar', 'b')
print(find_path(dikt, 'a', 'bar'))
print(dikt)

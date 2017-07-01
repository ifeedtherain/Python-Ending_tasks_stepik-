dikt = dict()

def add(n, v):
	if n in dikt:
		dikt[n].append(v)
	else:
		dikt[n]= [v]
def create(n, p):
	for k,v in dikt.items():
		if k == p:
			g = {n : 'None'}
			dikt[k].append(dict(g))

add('global', 'a')
create('foo', 'global')

print(dikt)
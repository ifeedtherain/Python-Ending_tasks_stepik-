graph = {}
for i in range(int(input())):
	x = input().split(':')
	if len(x) == 1:
		graph[x[0]] = x[0]
		continue
	if x[0] in graph.keys():
		x_temp = x[1].replace(' ', '')
		h = []
		if len(x_temp)>1:
			for i in x_temp:
				h.append(i)
			graph[x[0].replace(' ', '')] += h
		else:
			graph[x[0].replace(' ', '')] += x_temp
	else:

		x_temp = x[1].replace(' ', '')
		h = []
		if len(x_temp) > 1:
			for i in x_temp:
				h.append(i)
			graph[x[0].replace(' ', '')] = h
		else:
			graph[x[0].replace(' ', '')] = x_temp
massive = []
# def family(par,chld):
#     global massive
#     if graph.keys(chld) == "None":
#
#     if chld not in graph.keys():
#         return 'no'
#     massive += graph[chld]
#     if (len(graph.get(chld))) > 1:
#         for i in graph[chld]:
#             family(par,i)
#     return massive
def find_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if start not in graph.keys():
		return None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path)
			if newpath: return newpath
	return None

for k in range(int(input())):
	ge = input().split()
	print(find_path(graph, ge[0], ge[1]))


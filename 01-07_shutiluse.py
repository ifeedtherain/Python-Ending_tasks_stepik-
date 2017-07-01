import os
import os.path
import shutil
ans = []
temp = dict()
h = dict()
for current_dir, dirs, files in os.walk('./main'):
	temp[current_dir[2:]] = files
	h.update(temp)

for k,v in h.items():
	for j in v:
		if j.endswith('.py'):
			ans.append(k)

for i in sorted(set(ans)):
	print(i)
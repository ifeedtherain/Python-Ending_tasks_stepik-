#1
# f = input().lower().split()
# lst = dict()
# for i in f:
#     if i not in lst.keys():
#         lst[i] = 1
#     elif i in lst.keys():
#         lst[i] +=1
# for k,v in lst.items():
#     print(k, v)

#2 very bad I think, wonder if I could replace check on 'if i == 1,2 and >3',
# cheater!
f = int(input())
ls = []
tmp = []
for i in range(1,f):
    ls.append((str(i)*i))
for i in ls:
    for j in i:
        tmp.append(j)
if len(tmp) > 3:
    while len(tmp) != f:
        tmp.pop()
if f == 1:
    print('1')
if f == 2:
    print('1 2')
if f >= 3:
    print(*tmp)
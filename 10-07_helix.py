s = int(input())
d=[]
mx = []
for i in range(s):
    mx.append([0 for i in range(s)])
for i in range(pow(s,2)+1):
    if i == 0:
        i+=1
    else:
        d.append(i)
print(d)
print(mx)
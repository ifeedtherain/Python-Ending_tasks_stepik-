s = str(input())
t = str(input())
cnt = 0
def cnt_occur(s, t, cnt):
    i = -1
    while True:
        i = s.find(t, i+1)
        if i == -1:
            return cnt
        cnt += 1
if t in s:
    print(cnt_occur(s,t, cnt))
else:
    print(cnt)
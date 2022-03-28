#스택 수열

N = int(input())
Stack_List = []
start = 1
res = []
tf = 0

for i in range(N):
    num = int(input())
    while start <= num:
        Stack_List.append(start)
        res.append('+')
        start += 1
    if Stack_List[-1] == num:
        Stack_List.pop()
        res.append('-')
    else:
        print('NO')
        tf = 1
        break
if tf == 0:
    for i in res:
        print(i)

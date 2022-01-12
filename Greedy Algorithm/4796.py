#캠핑
i = 0
while(1):
    i += 1
    L, V, P = map(int,input().split())
    if L == 0 and  V == 0 and P == 0:
        break
    res = (P//V)*L
    res += min((P%V, L))
    print("Case %d: %d" %(i, res) )

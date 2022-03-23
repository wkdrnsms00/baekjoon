def checking(a):
    n = len(a)
    res = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if a[i][j] == a[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > res:
                res = cnt

        for j in range(1, n):
            if a[j][i] == a[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > res:
                res = cnt
    return res

N = int(input())
Bomboni = [list(input()) for _ in range(N)]
max = 0

for i in range(N):
    for j in range(N):
        if j+1 < N:
            Bomboni[i][j], Bomboni[i][j+1] = Bomboni[i][j+1], Bomboni[i][j]
            temp = checking(Bomboni)
            if temp > max:
                max = temp
            Bomboni[i][j], Bomboni[i][j+1] = Bomboni[i][j+1], Bomboni[i][j]

        if i+1 < N:
            Bomboni[i][j], Bomboni[i+1][j] = Bomboni[i+1][j], Bomboni[i][j]
            temp = checking(Bomboni)
            if temp > max:
                max = temp
            Bomboni[i][j], Bomboni[i+1][j] = Bomboni[i+1][j], Bomboni[i][j]
print(max)

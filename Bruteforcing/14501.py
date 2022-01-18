#퇴사
N = int(input())
M = [list(map(int, input().split()))for i in range(N)]
result = [0]


def bf(start, r):
    global result

    for i in range(start, N):
        if i+M[i][0] <= N:
            temp = bf(i+M[i][0], r+M[i][1])
            result.append(temp)
    return r

bf(0,0)
print(max(result))
# 블랙잭
N, M = map(int, input().split())
card = list(map(int, input().split()))

res = 0
for i in range(N):
    for j in range(i+1, N):
        for z in range(j+1, N):
            if card[i] + card[j] + card[z] > M:
                continue
            else:
                res = max(res, card[i] + card[j] + card[z])
print(res)
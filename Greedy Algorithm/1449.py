#수리공 항승

from sys import stdin

N, L = map(int, stdin.readline().split())
P = list(map(int,stdin.readline().split()))
P.sort()
start = P[0]
end = P[0]+ L
cnt = 1
for i in range(N):
    if start <= P[i] <end:
        continue
    else:
        start = P[i]
        end = P[i] + L
        cnt += 1
print(cnt)

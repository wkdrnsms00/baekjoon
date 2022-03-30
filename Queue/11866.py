#요세푸스 문제 0

from sys import stdin
from collections import deque
N, K = map(int,stdin.readline().split())
DQ = deque(list(range(1, N+1)))
res = []
while DQ:
    for i in range(K-1):
        DQ.append(DQ.popleft())
    res.append(DQ.popleft())

print("<",end='')
for i in range(len(res)-1):
    print("%d, " %res[i], end='')
print(res[-1], end='')
print(">")


#카드2

from sys import stdin
from collections import deque

N = int(stdin.readline())
Q = deque([])
for i in range(1, N+1):
    Q.append(i)

while 1:
    if len(Q) == 1:
        print(Q[0])
        break
    Q.popleft()
    num = Q.popleft()
    Q.append(num)
# 체인

from sys import stdin
from collections import deque

N = int(stdin.readline())
N_list = deque(sorted(list(map(int, stdin.readline().split()))))
cnt = 0 

while 1:
    N_list[0] -= 1
    cnt +=1
    A = N_list.pop()
    B = N_list.pop()
    N_list.append(A+B)
    if N_list[0] == 0:
        N_list.popleft()
    if len(N_list) == 1:
        break
print(cnt)


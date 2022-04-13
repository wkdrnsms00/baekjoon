#등수 매기기

from sys import stdin

N = int(stdin.readline())
N_list = [int(stdin.readline()) for _ in range(N)]
res = 0
N_list.sort()

for i in range(1, N+1):
    res += abs(i-N_list[i-1])
print(res)

#수 정렬하기 2
#stdin 사용
from sys import stdin
N = int(stdin.readline())
N_list = []
for i in range(N):
    num = int(stdin.readline())
    N_list.append(num)

N_list.sort()
for i in N_list:
    print(i)

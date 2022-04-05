#좌표 정렬하기
from sys import stdin

N = int(stdin.readline())
N_list = []
for i in range(N):
    N_list.append(list(map(int, stdin.readline().split())))

N_list.sort()
for i in range(len(N_list)):
    print(N_list[i][0], end=' ')
    print(N_list[i][1])
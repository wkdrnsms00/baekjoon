# 수 찾기

from sys import stdin

N = int(stdin.readline())
N_list = set(map(int, stdin.readline().split()))
M = int(stdin.readline())
M_list = list(map(int, stdin.readline().split()))

for i in range(M):
    if M_list[i] in N_list:
        print('1')
    else:
        print('0')
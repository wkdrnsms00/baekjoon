# 나이순 정렬
from sys import stdin

N = int(stdin.readline())
N_list = []
for i in range(N):
    N_list.append(list(stdin.readline().split()))
N_list.sort(key= lambda x:int(x[0])) # 나이 정수로 받아야되는 듯 int()안하니까 틀림

for i in range(len(N_list)):
    print(N_list[i][0], N_list[i][1])

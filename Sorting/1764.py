#듣보잡
# ------------------- 시간초과 ----------------------
# from sys import stdin

# N, M = map(int,stdin.readline().split())
# N_list = sorted(list(stdin.readline() for i in range(N)))
# M_list = sorted(list(stdin.readline() for i in range(M)))
# res = []

# for i in range(N):
#     if  N_list[i] in M_list:
#         res.append(N_list[i])

# print(len(res))    
# for j in range(len(res)):
#     print(res[j], end='')
#----------------------------------------------------------
from sys import stdin

N, M = map(int,stdin.readline().split())
N_list = set(stdin.readline() for i in range(N))
M_list = set(stdin.readline() for i in range(M))

res = sorted(list(N_list & M_list))
print(len(res))
for i in range(len(res)):
    print(res[i], end='')
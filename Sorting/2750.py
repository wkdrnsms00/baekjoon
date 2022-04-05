#수 정렬하기

N = int(input())
N_list = []
for i in range(N):
    num = int(input())
    N_list.append(num)

N_list.sort()
for i in N_list:
    print(i)

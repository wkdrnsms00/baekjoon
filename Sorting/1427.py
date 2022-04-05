# 소트인사이드
# 정수-> 리스트(내림차순)
N = int(input())
N_list = []
for i in str(N):
    N_list.append(i)
N_list.sort(reverse=True)
for i in range(len(N_list)):
    print(N_list[i], end='')
#좌표 정렬하기 2
from sys import stdin

N = int(stdin.readline())
N_list = []
for i in range(N):
    N_list.append(list(map(int, stdin.readline().split())))
N_list.sort()
N_list.sort(key=lambda x:x[1]) # 배열의 두 번째 요소를 오름차순 정렬 첫 번째 요소는 sort 사용해도됨 아니면 lambda x:x[0] 사용
for i in range(len(N_list)):
    print(N_list[i][0], end=' ')
    print(N_list[i][1])
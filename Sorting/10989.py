# 수 정렬하기 3
from sys import stdin

# N = int(stdin.readline())
# N_list = []

# for i in range(N):
#     N_list.append(int(stdin.readline()))

# N_list.sort()

# for i in range(len(N_list)):
#     print(N_list[i])
# 메모리 초과 코드
# for문에 append 사용시 메모리 재할당이 이루어져서 메로리를 효율적으로 사용못함

N = int(stdin.readline())
N_list = [0] * 10001

for _ in range(N):
    N_list[int(stdin.readline())] += 1

for i in range(10001):
    if N_list[i] != 0:
        for j in range(N_list[i]):
            print(i)
# 10000보다 작거나 같은 자연수, 배열은 0부터 시작이니까 10001개의 배열생성 (인덱스 0은 무시)
#회의실 배정
N = int(input())
time = []
for i in range(N):
    start , end = list(map(int, input().split()))
    time.append([start, end])

time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])

cnt = 0
last = 0
for i, j in time:
    if i >= last:
        cnt = cnt + 1
        last = j
print(cnt)



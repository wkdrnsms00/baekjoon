# 회전하는 큐
from sys import stdin
from collections import deque

def first_pop(list):
    list.popleft()
    return list
def right_shift(list): #양수 오른쪽으로 회전
    list.rotate(1)
    return list
def left_shift(list):
    list.rotate(-1)
    return list
    
N, M = map(int, stdin.readline().split())
target = list(map(int, stdin.readline().split()))
Q = deque(range(1, N+1))
cnt = 0
for i in target:
    while(1):
        if Q[0] == i:
            first_pop(Q)
            break
        else:
            if Q.index(i) < len(Q)/2:
                while Q[0] != i:
                    left_shift(Q)
                    cnt += 1
            else:
                while Q[0] != i:
                    right_shift(Q)
                    cnt += 1

print(cnt)


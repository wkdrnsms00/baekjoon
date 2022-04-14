#카약과 강풍

from sys import stdin

N ,S ,R = map(int, stdin.readline().split())
M = list(map(int, stdin.readline().split()))
P = list(map(int, stdin.readline().split()))

temp = [1 for _ in range(N)]

for i in range(len(M)):
    temp[M[i]-1] -= 1
for i in range(len(P)):
    temp[P[i]-1] +=1

for i in range(len(temp)):
    if temp[i] == 0:
        if i == 0:
            if temp[i+1] == 2:
                temp[i+1] = 1
                temp[i] = 1
        elif i == len(temp)-1:
            if temp[i-1] == 2:
                temp[i-1] = 1
                temp[i] = 1
        else:
            if temp[i-1] == 2:
                temp[i-1] = 1
                temp[i] = 1
                continue
            if temp[i+1] == 2:
                temp[i+1] = 1
                temp[i] = 1
                continue
    else:
        continue

print(temp.count(0))


    




 
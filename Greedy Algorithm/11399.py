#ATM 
N = int(input())
P = list(map(int, input().split()))

P.sort()
sum = 0
res = 0
for i in range(N):
    sum = sum + P[i]
    res = res + sum
print(res)
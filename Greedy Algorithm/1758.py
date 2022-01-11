#알바생 강호
N = int(input())
price = []
sum = 0
res = 0
for i in range(N):
    price.append(int(input()))
price.sort(reverse = True)
for i in range(N):
    sum = price[i] - (i)
    if sum >= 0:
        res = res + sum
print(res)
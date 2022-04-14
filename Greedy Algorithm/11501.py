# 주식

#----------------시간 초과 코드-------------------------------
# from sys import stdin
# from collections import deque

# T = int(stdin.readline())
# res = 0
# for i in range(T):
#     day = int(stdin.readline())
#     price = deque(list(map(int, stdin.readline().split())))
#     for _ in range(day):
#         high = price.index(max(price))
#         res += max(price) - price[0]
#         price.popleft()
#     print(res)
#     res = 0 
# -------------------------------------------------------------

from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    day = int(stdin.readline())
    res = 0
    price = list(map(int, stdin.readline().split()))

    while len(price) != 0:
        value = price.pop()
        for i in range(len(price)-1, -1, -1):
            if value > price[i]:
                res += (value - price[i])
                price.pop()
            else:
                break
    print(res)




         

         

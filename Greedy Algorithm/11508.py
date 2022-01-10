# 2+1 세일
# N = int(input())
# temp = []
# res = 0
# for i in range(N):
#     temp.append(int(input()))

# a = len(temp)//3
# b = len(temp)%3

# for i in range(a):
#     res = res + sum(temp[0:3]) - min(temp[0:3])
#     for j in range(3):
#         temp.pop(0)
# for i in range(b):
#     res = res + temp[b]
#     temp.pop[b]

# print(res) 런타임 에러 코드

N = int(input())
temp = []
for i in range(N):
    temp.append(int(input()))
temp.sort(reverse = True)

result = 0
for i in range(N):
    if i % 3 != 2:
        result += temp[i]
print(result)
 

# 주유소
# N = int(input()) 처음 코드
# Length = list(map(int, input().split()))
# City = list(map(int, input().split()))
# City.pop(N-1)
# price = 0
# for i in range(N-1):
#     if City[i] == min(City):
#         for j in range(i, N-1):
#             price = price + City[i] * Length[j]
#         break
#     else:
#         price = price + City[i]*Length[i]
# print(price)

N = int(input())
Length = list(map(int, input().split()))
City = list(map(int, input().split()))
res = 0

c = City[0]
for i in range(N-1):
    if c> City[i]:
        c= City[i]
    res = res + c* Length[i]
print(res)
    

        



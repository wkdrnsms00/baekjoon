# 2+1 세일

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
 

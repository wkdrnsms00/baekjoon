# 제로

N = int(input())
Zero_list = []
Sum = 0

for i in range(N):
    value = int(input())
    if value == 0:
        Zero_list.pop()
    else:
        Zero_list.append(value)
print(sum(Zero_list))



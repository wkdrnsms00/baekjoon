#괄호
N = int(input())

for i in range(N):
    Stack_List = list(input())
    sum = 0
    for j in Stack_List:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES') 

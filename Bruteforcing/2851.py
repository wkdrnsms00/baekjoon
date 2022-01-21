#슈퍼마리오
Mushroom = [int(input()) for _ in range(10)]
sum = 0
temp = 0 # 이전 sum
for i in range(10):
    sum += Mushroom[i]
    if sum >= 100:
        if sum - 100 > 100 - (sum - Mushroom[i]):
            sum -= Mushroom[i]
        break
print(sum)

    
        
    
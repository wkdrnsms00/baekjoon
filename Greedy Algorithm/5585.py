#거스름돈
N = int(input())
cnt = 0
price = 1000-N  
num = [500,100,50,10,5,1]
for i in range(len(num)):
    cnt = cnt + price//num[i] 
    price = price%num[i]
print(cnt) 
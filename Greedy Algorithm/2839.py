#3, 5킬로 봉지로 N킬로 배달
#3, 5로 못나누면 -1 리턴
#3, 5로나눠 나머지가 3, 0 일 때 두 경우중 적은 수 의 봉지를 얻을 수 있는 알고리즘
N = int(input())
res = 0
while N>=0: 
    if N%5 == 0:
        res = res + N//5 
        print(res)
        break
    N = N - 3
    res = res + 1
else: # while 판정이 거짓일 때 -1 출력 
    print("-1")

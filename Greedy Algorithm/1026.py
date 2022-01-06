#실버4 보물 
# 정렬해서 푸는 방법도 있음 sort (B의 배열은 건들 수 없기에 사용 X)
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0
for i in range(N):
    sum = sum +min(A)* max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
print(sum)



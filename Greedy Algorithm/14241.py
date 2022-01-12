#슬라임 합치기
#크기, 점수

N = int(input())
K = list(map(int, input().split()))
Size = K[0]
Score = 0
sum = 0
for i in range(1, N):
    sum = Size + K[i]
    Score = Score + Size * K[i]
    Size = sum

print(Score)

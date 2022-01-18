#덩치
N = int(input())
M = []

for _ in range(N):
    weight, height = map(int, input().split())
    M.append((weight, height))
for i in M:
    rank = 1
    for j in M:
        if i[0]< j[0] and i[1]< j[1]:
            rank += 1
    print(rank, end=" ")

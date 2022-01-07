#사과 담기 게임
N, M = map(int, input().split())
j = int(input())
apple = []
for i in range(j):
    apple.append(int(input()))

move = 0
start = 1
end = M

for i in range(j):
    if start <= apple[i] and end >= apple[i]:
        continue
    elif end < apple[i]:
        move += apple[i] - end
        end = apple[i]
        start = apple[i] - (M -1)
    elif start > apple[i]:
        move += start - apple[i]
        start = apple[i]
        end = apple[i] + (M - 1) 
print(move)
#박 터뜨리기 
N, K = map(int, input().split())
a = K*(K+1)//2

if (N - a)%K == 0:
    print(K-1)
elif a > N:
    print(-1)
else:
    print(K)
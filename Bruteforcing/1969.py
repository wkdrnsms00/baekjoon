#DNA
#Hamming Distance
N, M = map(int, input().split())
seq = [input() for i in range(N)]
result = ''
cnt = 0

for i in range(M):
    A = [0,0,0,0] # ATGC
    for j in range(N):
        if seq[j][i] == 'A':
            A[0] += 1
        elif seq[j][i] == 'T':
            A[1] += 1
        elif seq[j][i] == 'G':
            A[2] += 1
        elif seq[j][i] == 'C':
            A[3] += 1

    idx = A.index(max(A)) # max(A) 값이 있는 index 위치 idx
    if idx == 0:
        result += 'A'
    elif idx == 1:
        result += 'T'
    elif idx == 2:
        result += 'G'
    elif idx == 3:
        result += 'C'
    cnt += N -max(A)

print(result)
print(cnt)

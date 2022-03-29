# 프린터 큐(우선순위 있음)

N = int(input())
for i in range(N):
    n, m = map(int, input().split())
    Q = list(map(int, input().split()))
    Q_ = [0 for _ in range(n)]
    Q_[m] = 1
    cnt = 0
    while(1):
        if Q[0] == max(Q):
            cnt += 1
            if Q_[0] == 1:
                print(cnt)
                break
            else:
                Q.pop(0)
                Q_.pop(0)
        else:
            Q.append(Q[0])
            Q.pop(0)
            Q_.append(Q_[0])
            Q_.pop(0)

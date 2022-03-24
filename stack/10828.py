# 스택 구현
def push(sol ,X):
    sol.append(X)
    return sol

def pop(sol):
    if len(sol) == 0:
        print(-1)
    elif len(sol) != 0:
        print(sol.pop())
    return sol

def size(sol):
    print(len(sol))
    return sol

def empty(sol):
    if len(sol) == 0:
        print(1)
    else:
        print(0)
    return sol

def top(sol):
    if len(sol) == 0:
        print(-1)
    else:
        print(sol[len(sol)-1])
    return sol

N = int(input())
sol = []
task = [list(input().split()) for _ in range(N)]
for i in range(N):
    if task[i][0] == 'push':
        push(sol, task[i][1])
    elif task[i][0] == 'pop':
        pop(sol)
    elif task[i][0] == 'size':
        size(sol)
    elif task[i][0] == 'empty':
        empty(sol)
    else:
        top(sol)




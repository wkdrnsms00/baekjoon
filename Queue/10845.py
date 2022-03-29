# 큐
from sys import stdin

def push (list, num):
    list.append(num)
    return list

def pop (list):
    if len(list) == 0:
        print('-1')
    else:
        print(list.pop(0))
    return list

def size(list):
    print(len(list))
    return list

def empty(list):
    if len(list) == 0:
        print('1')
    else:
        print('0')
    return list

def front(list):
    if len(list) == 0:
        print('-1')
    else:
        print(list[0])
    return list

def back(list):
    if len(list) == 0:
        print('-1')
    else:
        print(list[-1])
    return list

 
N = int(stdin.readline())
data = []
for i in range(N):
    Q = stdin.readline().split()
    if Q[0] == 'push':
        push(data, Q[1])
    elif Q[0] == 'pop':
        pop(data)
    elif Q[0] == 'size':
        size(data)
    elif Q[0] == 'empty':
        empty(data)
    elif Q[0] == 'front':
        front(data)
    else:
        back(data)
    


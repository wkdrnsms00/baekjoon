#덱
from sys import stdin

def push_front(list, num):
    list.insert(0, num)
    return list
def push_back(list, num):
    list.append(num)
    return list
def pop_front(list):
    if len(list) == 0:
        print('-1')
    else:
        print(list.pop(0))
    return list
def pop_back(list):
    if len(list) == 0:
        print('-1')
    else:
        print(list.pop(-1))
    return list
def size(list):
    print(len(list))
    return list
def empty(list):
    if len(list) == 0:
        print('1')
    else:
        print('0')
def front(list):
    if len(list) == 0:
        print('-1')
    else:
        print(list[0])
def back(list):
    if len(list) == 0:
        print('-1')
    else:
        print(list[-1])

N = int(stdin.readline())
DQ = []
for i in range(N):
    data = stdin.readline().split()
    if data[0] == 'push_front':
        push_front(DQ ,data[1])
    elif data[0] == 'push_back':
        push_back(DQ, data[1])
    elif data[0] == 'pop_front':
        pop_front(DQ)
    elif data[0] == 'pop_back':
        pop_back(DQ)
    elif data[0] == 'size':
        size(DQ)
    elif data[0] == 'empty':
        empty(DQ)
    elif data[0] == 'front':
        front(DQ)
    else:
        back(DQ)
  
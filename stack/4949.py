# 균형잡힌 세상
from turtle import st


while(1):
    N = input()
    Stack_List = []

    if N == '.':
        break
    for i in N:
        if i =='(' or i =='[':
            Stack_List.append(i)
        elif i ==')':
            if len(Stack_List) != 0 and Stack_List[-1] == '(':
                Stack_List.pop()
            else:
                Stack_List.append(')')
                break
        elif i == ']':
            if len(Stack_List) != 0 and Stack_List[-1] == '[':
                Stack_List.pop()
            else:
                Stack_List.append(']')
                break
    if len(Stack_List) == 0:
        print('yes')
    else:
        print('no')
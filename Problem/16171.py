#나는 친구가 적다.
#---------------------------------
# from sys import stdin
# import re

# S = stdin.readline().strip('\n')
# K = stdin.readline().strip('\n')
# S = re.sub(r'[1-9]', "", S)
# if K in S:
#     print(1)
# else:
#     print(0)
#---------------------------------

from sys import stdin
S = stdin.readline().strip('\n')
K = stdin.readline().strip('\n')
temp = ''
for i in S:
    if i < '0' or i> '9':
        temp += i
if K in temp:
    print('1')
else:
    print('0')


    

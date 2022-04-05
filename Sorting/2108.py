#통계학

from sys import stdin
import math
from collections import Counter
def arithmetic_mean(list):
    global N
    return print(round(sum(list)/N))

def median(list):
    global N
    list.sort()
    res = math.floor(N/2)
    return print(list[res])

def Mode(list): # Collections Counter 
    cnt = Counter(list).most_common()
    if len(list) > 1:
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0])
        else:
            print(cnt[0][0])
    else:
        print(cnt[0][0])
    

def Range(list):
    return print(max(list)-min(list))

N = int(stdin.readline())
N_list = []
for i in range(N):
    N_list.append(int(stdin.readline()))

arithmetic_mean(N_list)
median(N_list)
Mode(N_list)
Range(N_list)

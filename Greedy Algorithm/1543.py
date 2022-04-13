#문서 검색

from sys import stdin

Document = stdin.readline()
target = stdin.readline()
res = 0
cnt = 0
while cnt <= len(Document) - len(target):
    if Document[cnt:cnt + len(target)] == target:
        res +=1
        cnt += len(target)
    else:
        cnt += 1
print(res)




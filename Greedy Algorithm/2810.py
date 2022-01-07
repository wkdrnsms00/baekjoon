#컵홀더
# 개인 S, 커플석 L
N = int(input())
cup = input()
cnt = cup.count('LL')
if cnt <=1:
    print(len(cup))
else:
    print(len(cup) - cnt + 1)

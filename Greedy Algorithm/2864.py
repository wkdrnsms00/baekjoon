# 5와 6의 차이
# 문자열 replace 사용해서 변경
A, B = input().split()

MIN = int(A.replace('6','5')) + int(B.replace('6', '5'))
MAX = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(MIN, MAX)
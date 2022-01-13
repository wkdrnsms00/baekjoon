#기타줄
N, M = map(int, input().split())
res = []
m_six = 1000
m_one = 1000

for i in range(M):
    a, b = map(int, input().split())
    m_six = min(m_six, a)
    m_one = min(m_one, b)


if m_one*6 >= m_six:
    if m_six*(N//6)+m_one*(N%6)>= m_six*(N//6+1):
        print(m_six*(N//6+1))
    else:
        print(m_six*(N//6)+m_one*(N%6))
elif m_one*6<= m_six:
    print(N*m_one)
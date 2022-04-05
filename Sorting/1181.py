#단어 정렬
# set 중복제거, 사전정렬, 길이정렬
N = int(input())
text_list = []
for i in range(N):
    text = input()
    text_list.append(text)
    
new_list = list(set(text_list))
new_list.sort()
new_list.sort(key=lambda x: len(x))

for i in range(len(new_list)):
    print(new_list[i])
#일곱 난쟁이
nine = [int(input()) for i in range(9)]
total = sum(nine)


for i in range(9):
    for j in range(i+1, 9):
        if total - (nine[i] + nine[j]) == 100:
            num1, num2 = nine[i], nine[j]
            nine.remove(num1)
            nine.remove(num2)
            nine.sort()
            for i in range(len(nine)):
                print(nine[i])
            break
    if len(nine)<9:
        break
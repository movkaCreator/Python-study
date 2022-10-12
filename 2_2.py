str = input()

sum = 0

for i in range(len(str)):
    if str[i].isdigit():
        sum += int(str[i])

print(sum)
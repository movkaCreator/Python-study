n = int(input())

maxIndex = -1
maxNum = -1

for index in range(n):
    num = int(input())
    if abs(num) >= maxNum:
        maxNum = abs(num)
        maxIndex = index

print(maxIndex + 1)
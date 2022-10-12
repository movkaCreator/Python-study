n = int(input())
List = list(map(int, input().split()))

maxNum = List[0]
maxIndex = 0

for i in range(n):
    if List[i] > maxNum:
        maxNum = List[i]
        maxIndex = i

List[maxIndex] = -List[maxIndex]

print(' '.join(map(str, List)))
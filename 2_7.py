List = list(map(int, input().split()))
numbers = list(map(int, input().split()))

sum = 0

for i in range(List[0]):
    if abs(numbers[i]) % 10 == List[2] and numbers[i] % List[1] != 0:
        sum += numbers[i]

print(sum)
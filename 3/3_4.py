n = int(input())
input = input().split()
result = []

for i in range(n):
    if len(input[i]) != len(set(input[i])):
        result.append(input[i])

print(' '.join(result))
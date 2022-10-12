n = int(input())

List = []

for i in range(n):
    List.append(int(input()))

k = int(input())

print(' '.join(map(str, list(map(lambda x: x * k, List)))))
s = input()
d = {}
result = []

for i in s:
    d[i] = d.get(i, 0) + 1

for i in d:
    if d.get(i) == 1:
        result.append(i)

print(''.join(sorted(result)))
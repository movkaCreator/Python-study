count = 1

for n in range(20):
    num = float(input())
    if (num >= 0):
        count *= num
    else:
        break

print(count)
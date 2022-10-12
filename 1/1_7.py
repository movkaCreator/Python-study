a, b = map(int, input().split())

count1 = 1
count2 = 1
total = 1
a1 = a

while a < b:
    a *= 3
    count1 += 1


while total < 1000000:
    a1 *= 3
    total += a1
    count2 += 1

print(count1, count2)
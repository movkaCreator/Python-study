n = int(input())

isPrime = True

for i in range(2, n // 2):
    if n % i == 0:
        isPrime = False
        break

if isPrime:
    print("Yes")
else:
    print("No")
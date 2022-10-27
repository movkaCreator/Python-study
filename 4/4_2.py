def isPrime(num):
    flag = True
    for i in range(2, num // 2):
        if num % i == 0:
            flag = False
            break
    return flag

num = int(input())

for i in range(1, num + 1):
    if isPrime(i) and isPrime(num - i):
        print(i, num - i)
        break
def classicFib(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return classicFib(k - 1) + classicFib(k - 2)

def fasterFib(k):
    a = 0
    b = 1
    for i in range(k):
        a = a + b
        b = a - b
    return a

k = int(input())
print(fasterFib(k))
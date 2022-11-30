def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def evensToZero(arr):
    for i in range(n):
        for j in range(m):
            if isEven(arr[i][j]):
                arr[i][j] = 0


n, m = map(int, input().split())
arrA = []
arrB = []

for i in range(n):
    arrA.append(list(map(int, input().split())))

for i in range(n):
    arrB.append(list(map(int, input().split())))

evensToZero(arrA)
evensToZero(arrB)

if arrA == arrB:
    print("YES")
else:
    print("NO")
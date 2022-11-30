n, m = map(int, input().split())

arr = [] 
for i in range(n): 
    arr.append(list(map(int, input().split())))

for j in range(m):
    min = arr[0][j]
    mini = 0
    minj = j
    for i in range(n):
        if arr[i][j] < min:
            min = arr[i][j]
            mini = i
            minj = j
    arr[mini][minj], arr[n - 1][j] = arr[n - 1][j], arr[mini][minj]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = ' ')
    print()
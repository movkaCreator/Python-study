n, m = map(int, input().split())

arr = [] 
for i in range(n): 
    arr.append(list(map(int, input().split())))

for j in range(m - 1):
    min = arr[0][j]
    mini = 0
    minj = j
    for i in range(n - 1):
        if arr[i][j] < min:
            min = arr[i][j]
            mini = i
            minj = j
    arr[mini][minj], arr[0][m - 1] = arr[0][m - 1], arr[mini][minj]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = ' ')
    print()



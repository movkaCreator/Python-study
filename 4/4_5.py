def transpose(arr):
    arrT = []
    for j in range(m):
        row = []
        for i in range(n):
            row.append(arr[i][j])
        arrT.append(row)
    return arrT
    

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

arrT = transpose(arr)

for i in range(len(arrT)):
    for j in range(len(arrT[i])):
        print(arrT[i][j], end = ' ')
    print()
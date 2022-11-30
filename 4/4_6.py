def zeroingArr(arr):
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        arr.append(row)

def multiplyArr(arr):
    tmp_arr = arr
    for count_pow in range(n - 1):
        result_arr = []
        zeroingArr(result_arr)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result_arr[i][j] += arr[i][k] * tmp_arr[k][j]
        tmp_arr = result_arr
    return result_arr

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(float, input().split())))

result_arr = multiplyArr(arr)

for i in range(len(result_arr)):
    for j in range(len(result_arr[i])):
        print('%.3f' % result_arr[i][j], end = ' ')
    print()
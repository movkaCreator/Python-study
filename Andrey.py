def fill_arr(num):
    arr = []
    index = 0
    while index * num <= money_sum:
        arr.append(index)
        index += 1
    return arr

def counter_var():
    counter = 0
    arr_a = fill_arr(abc[0])
    arr_b = fill_arr(abc[1])
    arr_c = fill_arr(abc[2])
    for i in range(len(arr_c)):
        for j in range(len(arr_b)):
            for k in range(len(arr_a)):
                if arr_a[k] * abc[0] + arr_b[j] * abc[1] + arr_c[i] * abc[2] == money_sum:
                        counter += 1
    return counter

abc = list(map(int, input().split()))
xyz = list(map(int, input().split()))

money_sum = abc[0] * xyz[0] + abc[1] * xyz[1] + abc[2] * xyz[2]

print(counter_var())
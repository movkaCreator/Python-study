import numpy as np

def inverse():
    file_input = open("input.txt", "r")
    file_output = open("output.txt", "w")
    flag = True
    size = int(file_input.readline())
    arr = []
    while flag:
        file_line = file_input.readline()
        if not file_line:
            file_input.close()
            flag = False
        else:
            arr.append(list(map(float, file_line.split())))

    np.set_printoptions(precision = 8, floatmode='fixed')
    result = np.linalg.inv(arr)
    for i in range(size):
        file_output.write(' '.join((str(format(j[i], '.8f')) for j in result)) + '\n')
    file_output.close()

inverse()
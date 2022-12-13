import numpy as np

def elementsMainDiagonal():
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
            arr.append(list(map(int, file_line.split())))

    result = np.diagonal(arr).tolist()
    file_output.write(' '.join(str(i) for i in result))
    file_output.close()
            
elementsMainDiagonal()
import numpy as np

def determinant():
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

    result = str(np.linalg.det(arr))
    file_output.write(result)
    file_output.close()
            
determinant()
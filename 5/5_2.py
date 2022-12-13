import numpy as np

def maxNumInColumn():
    file_input = open("input.txt", "r")
    file_output = open("output.txt", "w")
    flag = True
    size = int(file_input.readline())
    result = ""
    while flag:
        file_line = file_input.readline()
        if not file_line:
            file_output.write(result)
            file_input.close()
            file_output.close()
            return
        else:
            file_line = list(map(int, file_line.split()))
            result += str(np.max(file_line)) + ' '
            
maxNumInColumn()
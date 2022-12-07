def maxLengthRow():
    file_input = open("input.txt", "r")
    file_output = open("output.txt", "w")
    result = ""
    max = 0
    flag = True
    while flag:
        file_line = file_input.readline()
        if not file_line:
            file_output.write(result + str(max - 1))
            file_input.close()
            file_output.close()
            return
        elif file_line[0] =='\n':
            continue
        elif len(file_line) > max:
            result = file_line
            max = len(file_line)
            
print(maxLengthRow())
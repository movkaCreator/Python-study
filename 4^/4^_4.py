def numberOfMaxRow():
    file_input = open("input.txt", "r")
    file_output = open("output.txt", "w")
    max = 1
    flag = True
    while flag:
        file_line = file_input.readline()
        if not file_line:
            file_output.write(str(max - 1))
            file_input.close()
            file_output.close()
            return
        elif file_line[0] =='\n':
            continue
        elif len(file_line) > max:
            max = len(file_line)
            
print(numberOfMaxRow())
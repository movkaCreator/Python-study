def numberOfMaxRow():
    file_input = open("input.txt", "r")
    file_output = open("output.txt", "w")
    max = 1
    flag = True
    countRow = 0
    maxcount = 0
    while flag:
        file_line = file_input.readline()
        if not file_line:
            file_output.write(str(maxcount))
            file_input.close()
            file_output.close()
            return
        else:
            countRow += 1
            if len(file_line) > max:
                max = len(file_line)
                maxcount = countRow
            
print(numberOfMaxRow())
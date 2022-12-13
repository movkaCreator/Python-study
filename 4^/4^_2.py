def certainChars():
    file_input = open("input.txt", "r")
    file_output = open("output.txt", "w")
    k = int(file_input.readline())
    result = ""
    flag = True
    while flag:
        file_line = file_input.readline()
        if not file_line:
            file_output.write(result)
            file_input.close()
            file_output.close()
            return
        if len(file_line) < k:
            continue
        if file_line[k - 1] == '\n':
            continue
        else:
            result += file_line[k - 1]

certainChars()
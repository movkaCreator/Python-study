def firstChars():
    file_input = open("input.txt", "r")
    file_output = open("output.txt", "w")
    result = ""
    flag = True
    while flag:
        file_line = file_input.readline()
        if not file_line:
            file_output.write(result)
            file_input.close()
            file_output.close()
            return
        elif file_line == '\n':
            continue
        else:
            result += file_line[0]
            
print(firstChars())
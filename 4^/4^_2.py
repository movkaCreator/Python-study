def certainChars(k):
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
        elif len(file_line) < k:
            continue
        elif file_line[k] == ' ' or file_line[k] =='\n':
            continue
        else:
            result += file_line[k]

k = int(input())  
print(certainChars(k - 1))
def sort():
    file_input = open("input.txt", "r")
    file_output = open("output.txt", "w")
    flag = True
    while flag:
        file_line = file_input.readline()
        if not file_line:
            return
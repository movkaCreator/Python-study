def deleteBrackets(arr):
    for i in range(n):
        new_row = ""
        flag = True
        for char in rows[i]:
            if char == '(':
                flag = False
                continue
            elif char == ')':
                flag = True
                continue
            if flag:
                new_row += char
        rows[i] = new_row

n = int(input())
rows = []

for i in range(n):
    row = input()
    rows.append(row)

deleteBrackets(rows)

for i in range(n):
    print(rows[i])
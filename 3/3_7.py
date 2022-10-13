s1 = input()
s2 = input()
d = {}

for i in s1:
    d[i] = d.get(i, 0) + 1

flag = True

for i in range(len(s2)):
    if s2[i] in d:
        if d.get(s2[i]) != 0:
            d[s2[i]] -= 1
        else:
            flag = False
            print(flag)
            break
    else:
        flag = False
        print(flag)
        break

if flag:
    print(flag)
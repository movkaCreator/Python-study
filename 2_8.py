from cmath import pi, sqrt

List = list(input().split())

if List[0] == 'k':
    print(f'{float(List[1]) * pi * 2:.4f}', f'{float(List[1]) * float(List[1]) * pi:.4f}')
elif List[0] == 'p':
    print(f'{(float(List[1]) + float(List[2])) * 2:.4f}',
    f'{(float(List[1]) * float(List[2])):.4f}')
elif List[0] == 't':
    p = float((float(List[1]) + float(List[2]) + float(List[3])) / 2)
    print(f'{float(List[1]) + float(List[2]) + float(List[3]):.4f}',
    f'{(p * (p - (float(List[1]))) * (p - (float(List[2]))) * (p - (float(List[3])))) ** (0.5):.4f}')
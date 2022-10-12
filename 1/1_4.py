n = int(input())
word = "лет"

if (n // 10) % 10 != 1:
    if n % 10 == 1:
        word = "год"
    elif n % 10 in (2,3,4):
        word = "года"

print("Мне", n, word)
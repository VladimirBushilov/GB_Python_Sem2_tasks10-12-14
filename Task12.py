def find_numbers(S, P):
    for X in range(1, S+1):
        if P % X == 0 and (P // X) + X == S:
            return X, P // X

S = int(input("Введите сумму S: "))
P = int(input("Введите произведение P: "))

X, Y = find_numbers(S, P)
print("Задуманные числа Петей: X =", X, " и Y =", Y)
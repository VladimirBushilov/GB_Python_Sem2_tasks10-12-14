def print_powers_of_two(N):
    power = 0
    result = 1
    while result <= N:
        print(result)
        power += 1
        result = 2 ** power

N = int(input("Введите число N: "))
print("Целые степени двойки, не превосходящие", N, ":")
print_powers_of_two(N)
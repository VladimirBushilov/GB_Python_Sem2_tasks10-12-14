
def count_min_flips(coins):
    base_side = 1
    flips = 0

    for coin in coins:
        if coin != base_side:
            flips += 1

    return flips
coins = [0, 0, 1, 1, 0]
min_flips = count_min_flips(coins)
print(min_flips)

def count_ways_to_make_change(target, coins):
    ways = [0] * (target + 1)
    ways[0] = 1  # There is one way to make a change of 0 (using no coins)

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

target_amount = 200  # £2 in pence
coin_denominations = [1, 2, 5, 10, 20, 50, 100, 200]

result = count_ways_to_make_change(target_amount, coin_denominations)
print(f"There are {result} different ways to make £2.")

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin

    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    return dict(sorted(result.items()))

# Приклад використання:
sum_to_change = 113
print(f"Жадібний алгоритм для {sum_to_change}: {find_coins_greedy(sum_to_change)}")
print(f"Динамічне програмування для {sum_to_change}: {find_min_coins(sum_to_change)}")

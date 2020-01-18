"""
dp[i] = n # 兑换i元最少需要n次
if dp[i - coin] != -1 表明i-coin存在兑换方法
   dp[i] = 1 + min(coin in coins for dp[i-coin])  
"""


def coin_exchange(coins, target):

    if target == 0:
        return 0
    dp = [0 if init == 0 else -1 for init in range(target+1)]  # 严格注意此边界
    for i in range(1, target+1):
        h = target
        for coin in coins:
            if coin <= i and dp[i - coin] != -1:
                if dp[i - coin] <= h:
                    h = dp[i - coin]
        dp[i] = h + 1 if h < i + 1 else - 1
    return dp[target]


r = coin_exchange([1, 3, 5], 11)
print(r)

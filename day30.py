def coin_change(coins,amount):
    dp=[amount+1]*(amount+1)
    dp[0]=0
    for coin in coins:
        for x in range(coin,amount+1):
            dp[x]=min(dp[x],dp[x-coin]+1)
    return dp[amount] if dp[amount]!=amount+1 else -1
print(coin_change([1,2,5],11))
print(coin_change([2],3))
print(coin_change([1],0))

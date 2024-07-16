"""
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3


"""

"""
Approach 1 Greedy ??

 - Might not work - think why

"""

"""
Approach 2

 - memoization
"""

from typing import List

def coinChange(coins : List[int], amount : int) -> int :
    minCoin = [amount + 1] * (amount + 1)
    minCoin[0] = 0

    for a in range(1, amount + 1) :
        for coin in coins :
            if a - coin >= 0 :
                minCoin[a] = min(minCoin[a], 1 + minCoin[a - coin])
    
    if minCoin[amount] != amount + 1 :
        return minCoin[amount]
    else :
        return -1

coins = [1,7,2]
amount = 20
ans = coinChange(coins,amount)
print(ans)

"""
T(n) : O(amount * num of coins)
S(n) : O(amount)
"""
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""

"""
Approach 1 : Looping

- set default max profit to 0
- for each element:
 - compare the rest of the elements
 - if the diff is more than 0 -> update max profit
- return max profit 

"""

from typing import List


def buySellStock_App1 (prices : List[int]) -> int :
    
    maxProfit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > maxProfit :
                maxProfit = prices[j] - prices[i]

    return maxProfit

prices = [7,1,5,3,6,4]
prices = []

profit = buySellStock_App1(prices)
print(profit)


"""
T(n) : O(n^2)
S(n) : O(1)

"""
 
#########

"""
Approach 2 : Single Pass : Sliding Window


- set max profit to 0
- set a low pointer to 0
- set a high pointer to 1
- while h is less than len of price list
  - compare if price at high pointer is lower than price at low pointer
  - if yes update the low pointer at higher pointer 
  - else update max profit by taking max of max profit and current price diff
  - increment high pointer 

"""


def buySellStock_App2(prices :List[int]) -> int :
    maxProfit = 0
    l,h=0,1
    while h<len(prices) :
        if prices[l] > prices[h]:
            l=h
        else :
            maxProfit = max(maxProfit, prices[h] - prices[l])
        h+=1

    return maxProfit

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]

profit = buySellStock_App2(prices)
print(profit)







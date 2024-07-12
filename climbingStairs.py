"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

n = 2
Output: 2

Input: n = 3
Output: 3

"""

"""
Approach 1 : total sum = 1 + Sum(n-1)
"""

def climbStairs(n : int) -> int :
    oneStep = 1
    twoStep = 1

    for i in range(n -1) :
        temp = oneStep
        oneStep = oneStep + twoStep
        twoStep = temp
    return oneStep

ans = climbStairs(6)
print(ans)

"""
T(n) : O(n)
S(n) : O(n)
"""
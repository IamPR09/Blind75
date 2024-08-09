"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""




def validParenthesis(s : str) -> bool :
    parenthesisMap = {")" : "(",
                      "}" : "{",
                      "]" : "["}
    
    currentStack = []
    for char in s:
        if char in parenthesisMap:
            if currentStack and currentStack[-1] == parenthesisMap[char]:
                currentStack.pop()
            else:
                return False
        else:
            currentStack.append(char)
    return len(currentStack) == 0

s = s = "(]"
ans = validParenthesis(s)
print(ans)
        
"""
T(n) : O(n)
S(n) : O(n)
"""
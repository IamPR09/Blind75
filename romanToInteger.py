"""
Given a roman numeral, convert it to an integer.

"""


def romanToInt(s : str) -> int :
    output = 0
    romantoIntMap = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    } 

    for i  in range(len(s)) :
        if i < (len(s) - 1) and romantoIntMap[s[i]] < romantoIntMap[s[i+1]] :
            output -= romantoIntMap[s[i]]
        else :
            output += romantoIntMap[s[i]]
    
    return output

s = "MCMXCIV"
ans = romanToInt(s)
print (ans)



"""
T(n) : O(n)
S(n) :O(1)

"""
"""You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1.
 If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
"""


def mergeStringAlternately(word1 :str, word2 : str) -> str:
    resultString = ""
    for i in range(min(len(word1), len(word2))):
        resultString = resultString + word1[i] + word2[i]
    
    return resultString + word1[i+1:] + word2[i+1:]

word1 = "abc"
word2 = "p"
output = mergeStringAlternately(word1,word2)

print(output)

"""
T(n) -> O(m + n)
S(n) -> O(m + n)
"""



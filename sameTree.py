"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Input: p = [1,2,3], q = [1,2,3]
Output: true



"""


"""
Approach1 : recursive

- check if both tree exists
- check if val is same
- left is same
- right is same



"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    
class Solution:
    def isSameTree(self, p : Optional[TreeNode], q : Optional[TreeNode]) -> bool :
        if not p or not q :
            return False
        if not p and not q :
            return True
        if p and q :
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


"""
T(n) : O(m+n)
S(n) : O(h)

"""
          
        
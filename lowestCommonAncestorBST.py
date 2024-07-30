"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a 
descendant of itself).”

"""

"""

Approach 1 : Recursive

- make a pointer to current
- if p and q both are less than current node
  - look left
if p and q both are more than current node
 - look right
 - else return current pointer val 

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root : TreeNode, p : TreeNode, q : TreeNode) -> TreeNode :
    curr = root

    if curr.val < p.val and curr.val < q.val :
        curr = root.right 
    elif curr.val > p.val and curr.val > q.val :
        curr = root.left
    else :
        return curr


"""
T(n) : O(log n)
S(n) : O(1)
"""

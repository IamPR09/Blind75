"""
Given the root of a binary tree, invert the tree, and return its root.
root = [4,2,7,1,3,6,9]
"""


from typing import Optional

class TreeNode :
    def __init__(self, val, left = None, right = None) :
        self.left = left
        self.right = right
        self.val = val
    
def invertTree(self, root : Optional[TreeNode]) -> Optional[TreeNode] :
    if root is None :
        return None
    tmp = root.left
    root.left = root.right
    root.right = tmp

    self.invertTree(root.left)
    self.invertTree(root.right)
    return root

    
root = [4,2,7,1,3,6,9]
ans = invertTree(root)
print(ans)
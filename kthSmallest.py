"""
Given the root of a binary search tree, and an integer k,
 return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1


"""


"""
Approach 1 : InOrderTraversal


- visit the nodes in InOrder 
- keep appending the results in a list
- return k-1th element

# InOrder
               3
             /  \
            1    4
             \
              2

 - 1,2,3,4              
"""



def inOrderTraversal(r, inOrderList : list):
    if r is None :
        return
    inOrderTraversal(r.left)
    inOrderList.append(r.val)
    inOrderTraversal(r.right)
    return inOrderList



def kthSmallest(root : Optional[TreeNode], k:int) -> int:
    ans = []
    ans = inOrderTraversal(root, ans)
    return ans[k-1]

"""
T(n) : O(n)
S(n) : O(n)
"""



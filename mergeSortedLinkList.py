"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""

"""
Approach 1 : 2 pointer and compare 

- start with a dummy node pointing current pointer
- compare the elements in the list
- for each comparison while l1 and l2 exists :
  - if first element is small :
    - update the current pointers next to this val
    - increment l1
  - else :
    - update the current pointers next to be this val
    - increment l2
- check if l1 - the curent next is this list
- check if l2 - the current next is whole of this list
- return dummy.next

"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeSortedLinkList(l1 : Optional[ListNode], l2 : Optional[ListNode]) -> optional[ListNode] :
    dummy = ListNode()
    curr = dummy

    while l1 and l2 :
        if l1.val < l2.val :
            curr.next = l1
            l1 = l1.next
        else :
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1 :
        curr.next = l1
    else :
        curr.next = l2
    return dummy.next


"""
T(n) : o(n)
S(n) :O(1)
"""


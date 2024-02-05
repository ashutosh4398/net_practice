"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _recursive(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if node.next is None:
            return node, node

        new_head, next_node = self._recursive(node.next)
        next_node.next = node

        return new_head, node

    def _iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self._iterative(head)
        head, _ = self._recursive(head)
        return head
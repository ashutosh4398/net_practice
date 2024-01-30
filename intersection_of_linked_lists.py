"""
160 Intersection of Two Linked Lists
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_length(self, node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length
    
    def return_short_node(self, node, length):
        for i in range(length):
            node = node.next
        return node

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # len of list A
        len_a = self.get_length(headA)
        # len of list B
        len_b = self.get_length(headB)
        # which ever is longest, bring it's head such that both lists have same length
        if len_a > len_b:
            headA = self.return_short_node(headA, len_a - len_b)
        elif len_b > len_a:
            headB = self.return_short_node(headB, len_b - len_a)

        # then start comparing
        # once both are of equal length, then start comparing
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

        

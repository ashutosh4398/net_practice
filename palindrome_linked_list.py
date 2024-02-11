"""
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_length(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def print_list(self, head) -> None:
        while head:
            print(head.val, end = "  ")
            head = head.next
        print("\n")
        
    
    def reverse_linked_list(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def get_head_of_second_half(self, head: ListNode) -> ListNode:
        list_length = self.get_length(head)
        # reverse the second half of linked list
        second_list_head = head
        for _ in range(list_length//2):
            second_list_head = second_list_head.next
        
        if list_length % 2 != 0:
            return second_list_head.next
        return second_list_head

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first_half_head = head
        second_half_head = self.get_head_of_second_half(head)
        second_half_head = self.reverse_linked_list(second_half_head)
        while second_half_head and first_half_head:
            if second_half_head.val != first_half_head.val:
                return False
            second_half_head = second_half_head.next
            first_half_head = first_half_head.next
        return True


head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)

s = Solution()
# s.print_list(head)
print(s.isPalindrome(head))

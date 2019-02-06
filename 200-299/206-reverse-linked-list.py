# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	#recursive approach
    def reverseList(self, head: 'ListNode') -> 'ListNode':

        if not head or not head.next:
            return head

        cur = self.reverseList(head.next)
        head.next.next = head;
        head.next = None;
        
        return cur
        
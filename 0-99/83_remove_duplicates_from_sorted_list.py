# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Cleaner solution
        cur = head
        while cur and cur.next != None:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

        # My solution
        # main logic took about 11 mins
        # but then found error and took an aditional 15 min to debug
        # 'cur = prev ' was the solution
        cur = head
        while cur and cur.next != None:
            prev = cur
            cur = cur.next
            if cur.val == prev.val:
                prev.next = cur.next
                cur = prev
        return head
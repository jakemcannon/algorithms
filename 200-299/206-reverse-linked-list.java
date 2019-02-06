/**
 * Definition for singly-linked list
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {val = x; }
 * }
 */

class Solution {
    //recursive approach
    public ListNode reverseList(ListNode head) {
        
        ListNode cur = new ListNode(0);
        if (head == null || head.next == null) {
            return head;
        }
        
        cur = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        
        return cur;
    }
}
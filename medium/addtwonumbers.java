/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int currCarry = 0;
        int currSum = 0;
        ListNode result = new ListNode(0);
        ListNode head = result;
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                currSum = currCarry + l2.val;
                result.next = new ListNode(currSum % 10);
                result = result.next;
                currCarry = Math.floorDiv(currSum, 10);
                l2 = l2.next;
            } else if (l2 == null) {
                currSum = currCarry + l1.val;
                result.next = new ListNode(currSum % 10);
                result = result.next;
                currCarry = Math.floorDiv(currSum, 10);
                l1 = l1.next;
            } else {
                currSum = currCarry + l1.val + l2.val;
                result.next = new ListNode(currSum % 10);
                result = result.next;
                currCarry = Math.floorDiv(currSum, 10);
                l1 = l1.next;
                l2 = l2.next;
            }
        }
        if (currCarry > 0) {
            while (currCarry != 0) {
                result.next = new ListNode(currCarry % 10);
                result = result.next;
                currCarry = Math.floorDiv(currCarry, 10);
            }
        }
        return head.next;

    }
}

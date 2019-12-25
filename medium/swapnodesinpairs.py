class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmp = curr = ListNode(0)
        curr.next = head
        curr = curr.next
        while (curr != None and curr.next != None):
            curVal = curr.val
            nextVal = curr.next.val

            curr.val = nextVal
            curr.next.val = curVal
            curr = curr.next.next
        return tmp.next

    # Link: https://leetcode.com/problems/swap-nodes-in-pairs/

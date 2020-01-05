# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1) find if there is a cycle at all, slow fast pointers
        slow = fast = head
        if head is None:
            return None
        hasCycle = False
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break
        if not hasCycle:
            return None
        else:
        # 2) find the length of the cycle
            new = slow
            count = 0
            while True:
                new = new.next
                count += 1
                if new == slow:
                    break
            print(count)
            # 3) finally, create two new pointers, one that is len ahead of the other
            newSlow = newFast = head
            for i in range(count):
                newFast = newFast.next
        # 4) then move both pointers together until they are equal, that means that the fast pointer has made a complete loop, is now at the start of the cycle, and the slow pointer is also at the start of the cycle
            while newSlow != newFast:
                newSlow = newSlow.next
                newFast = newFast.next
            return newSlow


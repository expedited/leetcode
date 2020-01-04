class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = None
        isDistinct = None
        newDeleted = result = ListNode(0)
        result.next = head
        curr = head
        while curr != None:
            if prev == None:
                prev = curr.val
                isDistinct = True
            # prev stores the last item, a candidate that we only add when we realize it's distinct after seeing a new value
            elif prev != curr.val:
                # we figured out the last item was distinct, so we add it to our result list
                if isDistinct == True:
                    newDeleted = newDeleted.next
                    newDeleted.val = prev
                prev = curr.val
                isDistinct = True
            else:
                isDistinct = False
            curr = curr.next
        # corner case at the end, because curr will be None but the last candidate still hasn't been considered since we cut the loop already
        if isDistinct == True:
            newDeleted = newDeleted.next
            newDeleted.val = prev
        newDeleted.next = None
        return result.next

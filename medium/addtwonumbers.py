class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = ListNode(0)
        curr = res
        while l1 or l2:
            if not l1 or not l2:
                if not l1:
                    total = carry + l2.val
                    carry = total // 10
                    curr.next = ListNode(total % 10)
                    print(total % 10)
                    l2 = l2.next
                else:
                    total = carry + l1.val
                    carry = total // 10
                    curr.next = ListNode(total % 10)
                    l1 = l1.next
            else:
                total = carry + l1.val + l2.val
                carry = total // 10 
                curr.next = ListNode(total % 10)
                print(total % 10)
                l1 = l1.next
                l2 = l2.next
                
            curr = curr.next
                
        
        while carry != 0:
            curr.next = ListNode(carry % 10)
            carry = carry // 10
            curr = curr.next
                    
        return res.next
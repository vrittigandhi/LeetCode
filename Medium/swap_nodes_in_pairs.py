# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        final = ans = ListNode()
        count = 0
        if not head or not head.next:
            return head
        
        while head != None:
            count += 1
            if count % 2 != 0 and head.next:
                ans.val = head.next.val
                ans.next = ListNode()
                ans.next.val = head.val
                if head.next.next:
                    ans.next.next = ListNode()
                ans = ans.next.next
            elif count % 2 != 0:
                ans.val = head.val
            head = head.next
        
        return final

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_1 = []
        while l1:
            list_1.append(l1.val)
            l1 = l1.next
        while l2:
            list_1.append(l2.val)
            l2 = l2.next
        list_1.sort()
        ans = final = ListNode()
        if list_1 != []:
            final.val = list_1[0]
        
            for i in range(1,len(list_1)):
                final.next = ListNode()
                final.next.val = list_1[i]
                final = final.next
            return ans
        
        
        

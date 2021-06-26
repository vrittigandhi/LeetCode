# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_1 = []
        list_2 = []
        while l1:
            list_1.append(l1.val)
            l1 = l1.next
        while l2:
            list_2.append(l2.val)
            l2 = l2.next            
        list_1.reverse()
        list_2.reverse()
        add = int(''.join(map(str,list_1))) + int(''.join(map(str,list_2)))
        add_list = list(map(int,str(add)))
        add_list.reverse()
        ans = final = ListNode()
        final.val = add_list[0]
        
        for i in range(1,len(add_list)):
            final.next = ListNode()
            final.next.val = add_list[i]
            final = final.next
        
            
        print(final)
        return ans
        
        

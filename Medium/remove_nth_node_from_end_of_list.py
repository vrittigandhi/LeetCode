# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None
        count = 0
        head1 = head
        while head != None:
            head = head.next
            count += 1
        node = count - n + 1
        count_new = 0
        final = new_list = ListNode()
        if node > 1:
            new_list.val = head1.val 
        else:
            new_list.val = head1.next.val
        while head1 != None:
            count_new += 1
            if node != 1:
                if count_new not in (1, node) and head1 != None:
                    new_list.next = ListNode()
                    new_list.next.val = head1.val    
                    new_list = new_list.next
            else:
                if count_new not in (2, node) and head1 != None:
                    new_list.next = ListNode()
                    new_list.next.val = head1.val    
                    new_list = new_list.next
            head1 = head1.next
        return final

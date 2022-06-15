# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        tem = head
        while tem.next:
            if tem.val == tem.next.val: 
                tem.next = tem.next.next
            else: tem = tem.next
            
        return head
            
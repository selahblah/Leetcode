# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        if not head:
            return head
        
        while head and head.next == val:
            head = head.next
            
        cur = head
        
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head
        """
        
        while head and head.val == val:
            head = head.next
        
        if not head:
            return head
        
        next_node = head  
        while next_node and next_node.next:
            if next_node.next.val == val:
                next_node.next = next_node.next.next
            else:
                next_node = next_node.next
                
        return head
    
                
            
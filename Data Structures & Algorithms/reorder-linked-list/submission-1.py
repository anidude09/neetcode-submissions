# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        if head is None:
            return None

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        def reverse(node):
            if node is None:
                return None
            prev = None
            cur = node

            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            return prev

        first = head
        newstart = slow.next
        slow.next = None
        second = reverse(newstart)

        while second:
            n1 = first.next
            n2 = second.next
            first.next = second
            second.next = n1
            first = n1
            second = n2
        
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:




        heap = []
        count = 0

        for idx , nodelist in enumerate(lists):
            if nodelist:
                heapq.heappush(heap, (nodelist.val, count + 1, nodelist))
                count += 1
        
        dummy = ListNode()
        curr = dummy

        while heap:

            _, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next


            if node.next:
                heapq.heappush(heap, (node.next.val, count + 1, node.next))
                count += 1



        return dummy.next



        
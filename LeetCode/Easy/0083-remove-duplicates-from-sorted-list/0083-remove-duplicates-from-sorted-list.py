# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = head
        while head and head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            elif head.val != head.next.val:
                head = head.next
        
        return answer
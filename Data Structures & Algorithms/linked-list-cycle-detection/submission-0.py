# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        myset= set()
        while head and head.next:
            if head.next in myset:
                return True
            else:
                myset.add(head.next)
                head=head.next
        return False
        
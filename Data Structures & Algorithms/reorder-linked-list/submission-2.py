# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast=head, head
        while fast and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        prev, curr=None, slow.next
        slow.next=None
        while curr!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        list1,list2=head, prev
        while list2:
            temp2=list2.next
            temp1=list1.next
            list1.next=list2
            list2.next=temp1
            list1,list2=temp1, temp2

        


        

        

        

        
        
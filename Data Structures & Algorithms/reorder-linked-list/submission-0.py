# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
     l, r= head, head.next
     while  r and r.next:
        l=l.next
        r=r.next.next #segmentize into two halves
    
     second=l.next #Begining of the second list
     prev=l.next=None 
     while second: #reverse the direction of the second list
        temp=second.next
        second.next=prev
        prev=second
        second=temp
     first=head
     while prev:
        temp1=head.next
        temp2=prev.next
        head.next=prev
        prev.next=temp1
        prev, head=temp2, temp1


        
        
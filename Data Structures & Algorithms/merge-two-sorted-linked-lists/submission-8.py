# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode=newlist= ListNode()
        while list1 and list2:
            if list1.val<=list2.val:
                newlist.next=list1
                list1=list1.next
            else:
                newlist.next=list2
                list2=list2.next
            newlist=newlist.next
        if list1==None:
            newlist.next=list2
        else:
            newlist.next=list1
        return dummynode.next



        
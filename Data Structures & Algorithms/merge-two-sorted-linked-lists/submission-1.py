# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first_res=ListNode()
        current_res=first_res
        while list1:
            while list2 and list2.val <= list1.val:
                current_res.next=list2
                current_res=list2
                list2=list2.next
            current_res.next=list1
            current_res=list1
            list1=list1.next
        current_res.next=list2
        return first_res.next
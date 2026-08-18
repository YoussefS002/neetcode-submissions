# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reorder(head):
            if not head.next or not head.next.next:
                return head
            second=head.next
            before_last=head
            while before_last.next.next:
                before_last=before_last.next 
            last=before_last.next
            head.next=last
            last.next=second
            before_last.next=None
            second = reorder(second)
            return head
        reorder(head)
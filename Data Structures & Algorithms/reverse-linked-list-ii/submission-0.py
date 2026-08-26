# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pos=1
        current=head
        while pos<left:
            current=current.next
            pos+=1
        stack=[]
        while pos<=right:
            stack.append(current.val)
            current=current.next
            pos+=1
        pos=1
        current=head
        while pos<left:
            current=current.next
            pos+=1
        while pos<=right:
            current.val=stack.pop()
            current=current.next
            pos+=1
        return head
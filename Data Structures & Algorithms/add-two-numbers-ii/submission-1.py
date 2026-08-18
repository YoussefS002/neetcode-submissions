# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def invertList(l):
            stack=[]
            while l:
                stack.append(l.val)
                l=l.next
            start=None
            if stack:
                v=stack.pop()
                start=ListNode(val=v)
            current=start
            while stack:
                n=ListNode(val=stack.pop())
                current.next=n
                current=n
            return start
        l1 = invertList(l1)
        l2 = invertList(l2)
        start=None
        h=0
        if l1 and l2:
            v=l1.val+l2.val
            if v>9:
                h=1
            start=ListNode(val=v%10)
            l1=l1.next
            l2=l2.next
        current=start
        while l1 and l2:
            v=l1.val+l2.val+h
            if v>9:
                h=1
            else:
                h=0
            current.next=ListNode(val=v%10)
            current=current.next
            l1=l1.next
            l2=l2.next
        while l1:
            v=l1.val+h
            if v>9:
                h=1
            else:
                h=0
            current.next=ListNode(val=v%10)
            current=current.next
            l1=l1.next
        while l2:
            v=l2.val+h
            if v>9:
                h=1
            else:
                h=0
            current.next=ListNode(val=v%10)
            current=current.next
            l2=l2.next
        if h:
            current.next=ListNode(val=1)
        return invertList(start)

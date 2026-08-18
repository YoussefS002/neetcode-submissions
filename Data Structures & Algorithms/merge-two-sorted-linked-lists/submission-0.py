# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # res = []
        # list2_idx=0
        # for node in list1:
        #     if res:
        #         res[-1].next=list2[list2_idx]
        #     while list2[list2_idx].val <= node.val:
        #         res.append(list2[list2_idx])
        #         list2_idx+=1
        #     if res:
        #         res[-1].next=node
        #     res.append(node)
        # return res
        first_res=None
        current_res=None
        current1=list1
        current2=list2
        while current1:
            while current2 and current2.val <= current1.val:
                if first_res:
                    current_res.next=current2
                    current_res=current_res.next
                else:
                    first_res=current2
                    current_res=first_res
                current2=current2.next

            if first_res:
                current_res.next=current1
                current_res=current_res.next
            else:
                first_res=current1
                current_res=first_res

            current1=current1.next
        if not list1:
            return list2
        current_res.next=current2
        return first_res
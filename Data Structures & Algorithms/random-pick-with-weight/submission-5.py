import random 
class Solution:

    def __init__(self, w: List[int]):
        self.range_end=[]
        atom=1/sum(w)
        for i in range(len(w)):
            end=atom*w[i]
            if i:
                end+=self.range_end[i-1]
            self.range_end.append(end)
    def pickIndex(self) -> int:
        t=random.random()
        l=0
        r=len(self.range_end)-1
        while l<r:
            mid=l+(r-l)//2
            #l<=mid<mid+1<=r
            if self.range_end[mid]<t:
                l=mid+1
            else:
                r=mid
        return l
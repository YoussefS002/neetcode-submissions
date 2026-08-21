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
        r=random.random()
        for i in range(len(self.range_end)):
            if r<self.range_end[i]:
                return i
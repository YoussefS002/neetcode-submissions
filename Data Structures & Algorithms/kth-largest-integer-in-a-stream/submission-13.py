class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=sorted(nums)

    def add(self, val: int) -> int:
        if not (len(self.nums)>=self.k and val < self.nums[0]):
            l=0
            r=len(self.nums)
            while l<r: # O(log n) -> O(log k)
                mid = l + (r-l)//2 #<r
                if self.nums[mid]<val:
                    l=mid+1
                elif self.nums[mid]>val:
                    r=mid
                else:
                    l=mid
                    r=mid        
                
            self.nums.insert(l, val)
            if len(self.nums) > self.k:
                self.nums[-self.k:]
        return self.nums[-self.k]
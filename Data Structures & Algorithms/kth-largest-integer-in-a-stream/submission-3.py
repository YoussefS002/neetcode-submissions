class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=sorted(nums)

    def add(self, val: int) -> int:
        l=0
        r=len(self.nums)-1
        # while l<r:
        #     mid = l + (r-l)//2
        #     if self.nums[mid]<val:
        #         l=mid+1
        #     elif self.nums[mid]>val:
        #         r=mid-1
        #     else:
        #         l=mid
        #         r=mid
        idx=len(self.nums)
        for i in range(len(self.nums)):
            if self.nums[i]>val:
                idx=i
                break
        
        self.nums.insert(idx, val)
        return self.nums[-self.k]
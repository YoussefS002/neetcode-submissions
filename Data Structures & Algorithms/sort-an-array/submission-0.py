class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        n=len(nums)
        left = nums[:n//2]
        right = nums[n//2:]
        def merge(left, right):
            idx=0
            res=[]
            for x in left:
                while idx<len(right) and right[idx]<x:
                    res.append(right[idx])
                    idx+=1
                res.append(x)
            res+=right[idx:]
            return res
        return merge(
            self.sortArray(left),
            self.sortArray(right)
        )
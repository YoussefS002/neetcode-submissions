class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        res=0
        while l<=r:
            while r>=0 and nums[l]+nums[r]>target:
                r-=1
            if r>=l:
                res+=pow(2, r-l)%(1000000007)
            l+=1
        return res%(1000000007)
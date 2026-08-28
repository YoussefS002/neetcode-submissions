class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        res=0
        while l<=r:
            while r>=l and nums[l]+nums[r]>target:
                r-=1
            if r>=l:
                for i in range(l+1, r+1):
                    res+=pow(2, i-l-1)%(1000000007)
                res+=1
            l+=1
        return res%(1000000007)
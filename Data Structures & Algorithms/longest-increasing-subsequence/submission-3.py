class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[0 for i in range(len(nums))]
        dp[0]=1
        for i in range(1, len(nums)):
            m=0
            for j in range(i):
                if nums[i]>nums[j]:
                    m=max(m, dp[j])
            dp[i]=m+1
        return max(dp)
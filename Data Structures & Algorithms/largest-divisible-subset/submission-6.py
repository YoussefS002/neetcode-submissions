class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp=[[nums[0]]]
        max_idx=0
        max_len=1
        for i in range(1, len(nums)):
            biggest=0
            biggest_idx=None
            for j in range(i-1, -1, -1):
                if nums[i]%(dp[j][-1])==0:
                    if len(dp[j])>biggest:
                        biggest=len(dp[j])
                        biggest_idx=j
            if biggest_idx is not None:
                dp.append(dp[biggest_idx]+[nums[i]])
            else:
                dp.append([nums[i]])
            if len(dp[-1])>max_len:
                max_idx=i
                max_len=len(dp[i])
        return dp[max_idx]
        
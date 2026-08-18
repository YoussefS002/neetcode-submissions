class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            nums[i]=(i,num)
        nums.sort(key=lambda x : x[1])
        i=0
        j=len(nums)-1
        while nums[i][1]+nums[j][1]!=target:
            if nums[i][1]+nums[j][1]<target:
                i+=1
            else:
                j-=1
        return sorted([nums[i][0],nums[j][0]])
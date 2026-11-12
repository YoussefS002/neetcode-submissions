class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                new_target=target-(nums[i]+nums[j])
                l=j+1
                r=len(nums)-1
                while l<r:
                    if nums[l]+nums[r]==new_target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l+=1
                    elif nums[l]+nums[r]<new_target:
                        l+=1
                    else:
                        r-=1
        return list(res)
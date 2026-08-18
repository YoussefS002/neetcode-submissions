class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while nums[l]>nums[r]:
            mid=l+(r-l)//2
            if nums[l]<=nums[mid] and nums[mid+1]<=nums[r]:
                return nums[mid+1]
            if nums[l]<=nums[mid]:
                l=mid+1
            else:
                r=mid
        return nums[l]
            
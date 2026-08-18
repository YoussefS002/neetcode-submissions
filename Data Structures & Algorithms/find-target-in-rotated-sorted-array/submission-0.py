class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0, len(nums)-1
        while l<r:
            mid=(l+r)//2
            #l <= mid < mid+1 <= r
            if nums[l]<nums[r]:
                if target >= nums[mid+1]:
                    l=mid+1
                else:
                    r=mid
            else:
                if nums[mid+1]<=nums[r]:
                    if nums[mid+1]<=target<=nums[r]:
                        l=mid+1
                    else:
                        r=mid
                else:
                    if nums[l]<=target<=nums[mid]:
                        r=mid
                    else:
                        l=mid+1
        return l if nums[l]==target else -1
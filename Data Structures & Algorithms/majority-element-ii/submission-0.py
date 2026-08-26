class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mini=len(nums)//3+1
        res=[]
        h={}
        for num in nums:
            h[num]=h.get(num, 0)+1
            if h[num]==mini:
                res.append(num)
        return res
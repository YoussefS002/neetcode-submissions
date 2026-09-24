class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        contains_zero=False
        for num in nums:
            if num:
                p*=num
            else:
                if contains_zero:
                    return [0 for num in nums] 
                contains_zero=True
        res=[]
        for num in nums:
            if num:
                if contains_zero:
                    res.append(0)
                else:
                    res.append(p//num)
            else:
                res.append(p)
        return res
        
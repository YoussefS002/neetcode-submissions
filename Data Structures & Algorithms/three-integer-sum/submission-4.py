class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = sorted(nums)
        result = []
        i = 0
        while i < len(L):
            element = L[i]
            if element > 0:
                break
            need = -element
            rest = L[i+1:]
            if len(rest)<2:
                break
            l, r = 0, len(rest)-1
            while l < r:
                left = rest[l]
                right = rest[r]
                sum = left+right
                if sum == need:
                    result.append([element, left, right])
                if sum <= need:
                    while l < r and rest[l]==left:
                        l+=1
                elif sum > need:
                    while l < r and rest[r]==right:
                        r-=1
            while i < len(L) and L[i]==element:
                i+=1
        return result
                
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = sorted(nums)
        result = set()
        for i in range(len(L)):
            if L[i] > 0:
                break
            need = -L[i]
            rest = L[i+1:]
            if len(rest)<2:
                break
            l, r = 0, len(rest)-1
            while l < r:
                sum = rest[l]+rest[r]
                if sum == need:
                    result.add((L[i], rest[l], rest[r]))
                    l += 1
                if sum < need:
                    l+=1
                elif sum > need:
                    r -= 1
        return [list(x) for x in result]
                
            
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def aux(combination, currentSum, startingIdx):
            if currentSum > target:
                return
            if currentSum == target:
                res.append(combination)
                return
            for i in range(startingIdx, len(nums)):
                num=nums[i]
                aux(combination+[num], currentSum+num, i)
        aux([], 0, 0)
        return res
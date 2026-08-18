class Solution:
    def rob(self, nums: List[int]) -> int:
        mem={}
        def aux(last_house):
            if last_house in mem:
                return mem[last_house]
            if last_house==0:
                return nums[0]
            if last_house==1:
                return max(nums[0], nums[1])
            money_w_last = aux(last_house-2)+nums[last_house]
            money_wout_last = aux(last_house-1)
            mem[last_house] = max(money_w_last, money_wout_last)
            return mem[last_house]
        return aux(len(nums)-1)
            
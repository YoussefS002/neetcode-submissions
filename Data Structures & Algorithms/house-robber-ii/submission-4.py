class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        mem={}
        def aux(first_house, last_house):
            if last_house in mem:
                return mem[last_house]
            if last_house==first_house:
                return nums[first_house]
            if last_house==first_house+1:
                return max(nums[first_house], nums[first_house+1])
            money_w_last = aux(first_house, last_house-2)+nums[last_house]
            money_wout_last = aux(first_house, last_house-1)
            mem[last_house] = max(money_w_last, money_wout_last)
            return mem[last_house]
        right_to_last = aux(1, len(nums)-1)
        mem={}
        no_right_to_last = aux(0, len(nums)-2)
        return max(right_to_last, no_right_to_last)
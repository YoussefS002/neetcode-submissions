class Solution:
    def climbStairs(self, n: int) -> int:
        mem={}
        def aux(n):
            if n in mem:
                return mem[n]
            if n==1:
                return 1
            if n==2:
                return 2
            mem[n]=aux(n-1)+aux(n-2)
            return mem[n]
        return aux(n)
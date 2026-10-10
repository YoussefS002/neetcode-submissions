class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        res=0
        while i<len(height):
            water=0
            j=i+1
            max_height=0
            while j<len(height):
                if height[j]>=height[i]:
                    break
                else:
                    max_height=max(max_height, height[j])
                    water+=height[i]-height[j]
                    j+=1
            if j<len(height):
                res+=water
                i=j
            else:
                if max_height==0:
                    break
                height[i]=max_height
        return res
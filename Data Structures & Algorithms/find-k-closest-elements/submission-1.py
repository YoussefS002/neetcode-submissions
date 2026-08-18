class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        r=k-1
        for i in range(k, len(arr)):
            if abs(arr[i]-x)<abs(arr[l]-x):
                l+=1
                r+=1
            elif abs(arr[i]-x)==abs(arr[l]-x) and arr[i]==arr[l]:
                l+=1
                r+=1
            else:
                break
        return arr[l:r+1]

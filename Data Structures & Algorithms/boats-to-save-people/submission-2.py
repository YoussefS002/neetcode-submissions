class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        res=0
        while l<=r:
            space=limit-people[r]
            r-=1

            if r>=l and people[r]<=space:
                r-=1
            elif l<=r and people[l]<=space:
                l+=1
            res+=1
        return res

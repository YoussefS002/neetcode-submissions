class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        stack=sorted(list(set(hand)), reverse=True)
        h={}
        for card in hand:
            h[card]=h.get(card, 0)+1
        while stack:
            first=stack.pop()
            if not h[first]:
                continue
            for card in range(first+1, first+groupSize):
                if card not in h or h[card]<h[first]:
                    return False
                h[card]-=h[first]
            h[first]=0
        return True
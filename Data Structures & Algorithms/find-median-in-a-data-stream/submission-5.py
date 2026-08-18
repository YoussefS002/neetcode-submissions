class MedianFinder:

    def __init__(self):
        self.leftheap=[]
        self.rightheap=[]
        self.median=None

    def addNum(self, num: int) -> None:
        if not self.leftheap and not self.rightheap and self.median is None:
            self.median=num
            return
        if self.median is not None:
            if num <= self.median:
                heapq.heappush_max(self.leftheap, num)
                heapq.heappush(self.rightheap, self.median)
                self.median=None
            else:
                heapq.heappush(self.rightheap, num)
                heapq.heappush_max(self.leftheap, self.median)
                self.median=None
            return
        max_left=self.leftheap[0]
        min_right=self.rightheap[0]
        if num <= max_left:
            heapq.heappush_max(self.leftheap, num)
            self.median=heapq.heappop_max(self.leftheap)
        elif num >= min_right:
            heapq.heappush(self.rightheap, num)
            self.median=heapq.heappop(self.rightheap)
        else:
            self.median=num
        

    def findMedian(self) -> float:
        if self.median is not None:
            return self.median
        max_left=self.leftheap[0]
        min_right=self.rightheap[0]
        return (max_left+min_right)/2
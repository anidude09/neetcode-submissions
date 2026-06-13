class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(int(num))

    def findMedian(self) -> float:

        self.arr.sort()

        n = len(self.arr)
        if n <= 1: 
            return self.arr[0]

        if n%2 == 0 : 
            mid1, mid2 = int(n/2), int(n/2 - 1)
            return ((self.arr[mid1] + self.arr[mid2]) / 2)

        else : 
            return self.arr[n//2]



        
        
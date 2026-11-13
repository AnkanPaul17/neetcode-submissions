class Solution:
    def calWeight(self, mid, weights):
        totalDays=1
        weightInDay=0
        for i in range(len(weights)):
            weightInDay+=weights[i]
            if weightInDay>mid:
                totalDays+=1
                weightInDay=weights[i]
        return totalDays

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights)==0:
            return 0
        max_weight=0
        for i in range(len(weights)):
            max_weight+=weights[i]
        low=max(weights)
        high=max_weight
        ans=1
        while low<=high:
            mid=(low+high)//2
            capacity=self.calWeight(mid, weights)
            if capacity<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
            
        
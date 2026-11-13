class Solution:
    def eatingSpeed(self, speed, piles):
        output=0
        for i in range(len(piles)):
            if piles[i]<=speed:
                output+=1
            else:
                if piles[i]%speed==0:
                    output+=piles[i]//speed
                else:
                    output+=(piles[i]//speed)+1
        return output

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==0:
            return 0
        total=0
        for i in range(len(piles)):
            total+=piles[i]
        low=1
        high=total
        ans=1
        while low<=high:
            mid=(low+high)//2
            totalHoursTaken=self.eatingSpeed(mid, piles)
            if totalHoursTaken<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans



        
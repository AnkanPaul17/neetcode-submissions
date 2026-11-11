class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        c=0
        l=0
        r=len(people)-1
        while l<r:
            if limit-people[l]>=people[r]:
                c+=1
                l+=1
                r-=1
            else:
                r-=1
        c+=len(people)-2*c
        return c


        
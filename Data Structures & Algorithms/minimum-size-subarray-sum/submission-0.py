class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total=0
        l=0
        c=0
        min_c=2**31
        for i in range(len(nums)):
            total+=nums[i]
            c+=1
            while total>=target:
                min_c=min(c, min_c)
                total-=nums[l]
                l+=1
                c-=1
        if min_c==2**31:
            return 0
        else:
            return min_c

        
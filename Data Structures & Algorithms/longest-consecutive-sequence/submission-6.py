class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        max_c=0
        for i in nums_set:
            if i-1 not in nums_set:
                c=1
                while i+c in nums_set:
                    c+=1
                max_c=max(c, max_c)
        return max_c


        
             
        
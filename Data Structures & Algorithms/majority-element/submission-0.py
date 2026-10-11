import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        for i in freq:
            if freq[i]>math.floor(len(nums)//2):
                return i
        return 0
        
        
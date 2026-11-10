class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        for i in freq:
            if freq[i]>len(nums)//3:
                ans.append(i)
        return ans

        
        
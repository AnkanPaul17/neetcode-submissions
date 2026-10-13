class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        ans=[]
        for i in range(k):
            maxi=0
            element=-1
            for j in freq:
                if freq[j]>maxi and j not in ans:
                    maxi=freq[j]
                    element=j
            ans.append(element)
        return ans

        
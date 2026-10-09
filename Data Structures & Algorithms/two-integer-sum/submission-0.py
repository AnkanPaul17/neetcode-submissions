class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem={}
        for i in range(len(nums)):
            left=target-nums[i]
            if left not in rem:
                rem[nums[i]]=i
            else:
                return [rem[left], i]
        return [-1, -1]
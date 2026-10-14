class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix={}
        prefix_product=1
        postfix={}
        postfix_product=1
        output=[]
        for i in range(len(nums)):
            if i==0:
                prefix[i]=1
            else:
                prefix_product*=nums[i-1]
                prefix[i]=prefix_product
        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1:
                postfix[i]=1
            else:
                postfix_product*=nums[i+1]
                postfix[i]=postfix_product
        for i in range(len(nums)):
            output.append(prefix[i]*postfix[i])
        return output

        
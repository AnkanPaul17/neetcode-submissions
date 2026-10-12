class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, low, middle, high):
            temp=[]
            left=low
            right=middle+1
            while(left <=middle and right<=high):
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while(left <=middle):
                temp.append(nums[left])
                left+=1
            while(right<=high):
                temp.append(nums[right])
                right+=1
            for i in range(low, high+1):
                nums[i]=temp[i-low]
                
        def mergeSort(nums, low, high):
            if low>=high:
                return
            middle=(low+high)//2
            mergeSort(nums, low, middle)
            mergeSort(nums, middle+1, high)
            merge(nums, low, middle, high)
        
        mergeSort(nums, 0, len(nums)-1)
        return nums
        
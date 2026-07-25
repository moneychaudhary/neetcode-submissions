class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_items = len(nums)
        left = [1] * total_items
        for i in range(1, total_items):
            left[i] =  left[i-1] * nums[i - 1]
        
        right = [1] * total_items
        for j in range(total_items - 2, -1, -1):
            right[j] = right[j+1] * nums[j + 1]

        return [left[k] * right[k] for k in range(total_items)]
            

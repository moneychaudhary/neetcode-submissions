class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        total_nums = len(nums)
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            left = i + 1
            right = total_nums - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return output


        
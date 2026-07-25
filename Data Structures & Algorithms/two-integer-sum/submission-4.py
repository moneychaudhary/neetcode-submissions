class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        index_dict = {}
        for i in range(len(nums)):
            index_dict[target - nums[i]] = i

        for j in range(len(nums)):      
            second_index = index_dict.get(nums[j], -1)
            if second_index > j:
                return [j, second_index]

        
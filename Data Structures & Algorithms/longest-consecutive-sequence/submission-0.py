class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        uniq_nums = set(nums)
        for num in nums:
            if num - 1 not in uniq_nums:
                length = 1
                current = num
                while current + 1 in uniq_nums:
                    length = length + 1
                    current = current + 1
                max_len = max(max_len, length)
        return max_len            


        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = set()
        for num in nums:
            if num in exist:
                return True
            exist.add(num)
        return False
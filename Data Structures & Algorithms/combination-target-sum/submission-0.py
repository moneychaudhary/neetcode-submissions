class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.results = []
        self.uniq = set()
        def get_comb(index, nums, subset, target):
            if index == len(nums) or target < 0:
                return
            
            if target == 0:
                if tuple(subset) not in self.uniq:
                    self.results.append(subset.copy())
                    self.uniq.add(tuple(subset))
                return

            subset.append(nums[index])
            get_comb(index + 1, nums, subset, target - nums[index])
            get_comb(index, nums, subset, target - nums[index])
            subset.pop()
            get_comb(index + 1, nums, subset, target)

        get_comb(0, nums, [], target)
        return self.results
        
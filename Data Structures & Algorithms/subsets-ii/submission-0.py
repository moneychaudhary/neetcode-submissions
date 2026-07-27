class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.uniq = set()
        nums.sort()

        def get_subset(index, subset):
            if index == len(nums):
                if tuple(subset) not in self.uniq:
                    self.results.append(subset.copy())
                    self.uniq.add(tuple(subset))
                return

            subset.append(nums[index])
            get_subset(index + 1, subset)
            subset.pop()

            get_subset(index + 1, subset)

        get_subset(0, [])
        return self.results

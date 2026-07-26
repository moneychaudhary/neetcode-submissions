class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def find_subsets(index, nums, subset):
            if index == len(nums):
                self.result.append(subset.copy())
                return

            subset.append(nums[index])
            find_subsets(index + 1, nums, subset)
            subset.pop()

            find_subsets(index + 1, nums, subset)

        find_subsets(0, nums, [])
        return self.result

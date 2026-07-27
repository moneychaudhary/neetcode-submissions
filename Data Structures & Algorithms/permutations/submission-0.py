class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.uniq = set()

        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def get_perm(index, nums, perms):
            if index == len(nums):
                if tuple(nums) not in self.uniq:
                    self.results.append(nums.copy())
                    self.uniq.add(tuple(nums))
                return

            for i in range(len(nums)):
                swap(nums, i, index)
                get_perm(index + 1, nums, perms)
                swap(nums, i, index)

        get_perm(0, nums, [])
        return self.results

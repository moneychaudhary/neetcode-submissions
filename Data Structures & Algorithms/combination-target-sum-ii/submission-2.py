class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        self.uniq = set()
        candidates.sort()

        def comb(index, candidates, subset, target):
            if target == 0:
                if tuple(subset) not in self.uniq:
                    self.results.append(subset.copy())
                    self.uniq.add(tuple(subset))
                return

            if index == len(candidates) or target < 0:
                return

            subset.append(candidates[index])
            comb(index + 1, candidates, subset, target - candidates[index])
            subset.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            comb(index + 1, candidates, subset, target)

        comb(0, candidates, [], target)
        return self.results

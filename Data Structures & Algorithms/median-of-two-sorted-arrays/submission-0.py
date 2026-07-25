class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        smaller_array = nums1 if len(nums1) <= len(nums2) else nums2
        bigger_array = nums2 if len(nums1) <= len(nums2) else nums1

        total_nums = len(smaller_array) + len(bigger_array)
        partion_nums = total_nums // 2

        start = 0
        end = len(smaller_array)
        median = 0
        while start <= end:
            mid = (start + end) // 2
            second_mid = partion_nums - mid

            smaller_left = smaller_array[mid - 1] if mid > 0 else float('-inf')
            smaller_right = smaller_array[mid] if mid < len(smaller_array) else float('inf')
            bigger_left = bigger_array[second_mid - 1] if second_mid > 0 else float('-inf')
            bigger_right = bigger_array[second_mid] if second_mid < len(bigger_array) else float('inf')

            if smaller_left <= bigger_right and bigger_left <= smaller_right:
                if total_nums % 2:
                    return min(smaller_right, bigger_right)
                else:
                    return (max(smaller_left, bigger_left) + min(smaller_right, bigger_right)) / 2

            elif smaller_left > bigger_right:
                end = mid - 1
            else:
                start = mid + 1
        return median

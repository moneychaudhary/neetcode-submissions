class Solution:
    import math

    def need_hours(self, piles: List[int], k: speed):
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        needed_speed = max_speed

        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            needed_hours = self.need_hours(piles, mid_speed)
            if needed_hours <= h:
                needed_speed = mid_speed
                max_speed = mid_speed - 1
            else:
                min_speed = mid_speed + 1
        
        return needed_speed
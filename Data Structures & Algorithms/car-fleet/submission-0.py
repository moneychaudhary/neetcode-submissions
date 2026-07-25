class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for pos, speed in zip(position, speed):
            cars.append((pos, (target - pos) / speed))

        cars.sort(reverse=True)

        fleets = 0
        current_time = 0

        for pos, time in cars:
            if time > current_time:
                fleets += 1
                current_time = time

        return fleets

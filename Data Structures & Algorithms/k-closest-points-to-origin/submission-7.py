import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        distance_points_map = defaultdict(list)


        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(max_heap, -1 * distance)
            distance_points_map[distance].append(point)
            if len(max_heap) > k:
                distance = -1 * heapq.heappop(max_heap)
                distance_points_map[distance].pop()
        
        output = []
        for v in distance_points_map.values():
            output.extend(v)
        return output

        
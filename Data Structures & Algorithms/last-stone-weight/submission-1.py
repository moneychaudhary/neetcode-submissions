import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1 * s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x = -1 * heapq.heappop(max_heap)
            y = -1 * heapq.heappop(max_heap)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(max_heap, -1 * (y - x))
            else:
                heapq.heappush(max_heap, -1 * (x - y))
        
        if max_heap:
            return -1 * max_heap[0]
        return 0

        
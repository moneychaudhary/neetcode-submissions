class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq

        counter = Counter(tasks)

        max_heap = [-1 * c for c in counter.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()
        while max_heap or queue:
            time += 1
            if max_heap:
                count = -1 * heapq.heappop(max_heap) - 1
                if count:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, -1 * queue.popleft()[0])
        return time

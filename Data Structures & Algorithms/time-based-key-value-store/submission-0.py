class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        if not values:
            return ""
        start = 0
        end = len(values) - 1
        res = ""
        while start <= end:
            mid = (start + end) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return res
        

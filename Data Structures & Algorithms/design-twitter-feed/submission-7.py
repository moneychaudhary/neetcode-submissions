class Twitter:
    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                last_index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][last_index]
                heapq.heappush(max_heap, [count, tweetId, followeeId, last_index - 1])
        heapq.heapify(max_heap)
        output = []
        while len(output) < 10 and max_heap:
            count, tweetId, followeeId, index = heapq.heappop(max_heap)
            output.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(max_heap, [count, tweetId, followeeId, index - 1])
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_map[followerId]:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)

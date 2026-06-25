class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for tweet in self.tweets[userId]:
            heapq.heappush(heap, tweet)

        for followeeId in self.following[userId]:
            for tweet in self.tweets[followeeId]:
                heapq.heappush(heap, tweet)

        res = []

        while heap and len(res) < 10:
            time, tweetId = heapq.heappop(heap)
            res.append(tweetId)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
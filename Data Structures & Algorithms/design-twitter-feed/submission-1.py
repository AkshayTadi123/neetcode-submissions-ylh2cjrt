from collections import defaultdict

class Twitter:

    def __init__(self):
        self.order = 0
        self.heap = []
        heapq.heapify(self.heap)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.order += 1
        x = (-(self.order), userId, tweetId)
        heapq.heappush(self.heap, x)

    def getNewsFeed(self, userId: int) -> List[int]:
        new_heap = self.heap.copy()
        count = 0
        result = []
        while count != 10 and new_heap:
            x = heapq.heappop(new_heap)
            if x[1] == userId or x[1] in self.followers[userId]:
                result.append(x[2])
                count += 1

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)


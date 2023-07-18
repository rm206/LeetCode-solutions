from collections import defaultdict

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = []
        self.post_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.insert(0, [userId, tweetId])
        self.post_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        added = 0
        post_index = 0

        if self.post_count > 0:
            while added < 10 and post_index < self.post_count:
                posterId, tweetId = self.posts[post_index]
                if posterId in self.following[userId] or posterId == userId:
                    res.append(tweetId)
                    added += 1

                post_index += 1
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
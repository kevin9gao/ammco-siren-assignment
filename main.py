class User():
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.fav_movies = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def add_fav_movie(self, *movies):
        for movie in movies:
            self.fav_movies.append(movie)

def find_most_popular_movie(user):
    count = {}
    visited = set()

    def dfs(curr_user):
        visited.add(curr_user)
        for movie in curr_user.fav_movies:
            if movie not in count:
                count[movie] = 1
            else:
                count[movie] += 1
        for friend in curr_user.friends:
            if friend not in visited:
                dfs(friend)

    dfs(user)

    return max(count, key=count.get)

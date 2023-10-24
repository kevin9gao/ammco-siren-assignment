import unittest
from main import User, find_most_popular_movie

class TestPopularMovies(unittest.TestCase):
    def test_single_user(self):
        user = User('Kevin')
        user.add_fav_movie('Avengers: Endgame')
        popular = find_most_popular_movie(user)
        print(f'test_single_user: The most popular movie in {user.name}\'s network of friends is "{popular}".')
        self.assertEqual(popular, 'Avengers: Endgame', f"{user.name}'s favorite movie should be Avengers: Endgame")

    def test_multiple_users(self):
        user1 = User('Kevin')
        user2 = User('Dindin')
        user3 = User('Ahri')
        user4 = User('Derek')
        user5 = User('Joey')

        user1.add_friend(user2)
        user1.add_friend(user3)
        user1.add_friend(user4)
        user1.add_friend(user5)

        user1.add_fav_movie('Avengers: Endgame')
        user2.add_fav_movie('Shutter Island')
        user3.add_fav_movie('Shutter Island')
        user4.add_fav_movie('Shutter Island')
        user5.add_fav_movie('Avengers: Endgame')

        popular = find_most_popular_movie(user1)
        print(f'test_multiple_users: The most popular movie in {user1.name}\'s network of friends is "{popular}".')
        self.assertEqual(popular, 'Shutter Island', f"{user1.name}'s favorite movie within their network of friends should be Shutter Island.")

    def test_bidirectional_friendships(self):
        user1 = User('Kevin')
        user2 = User('Dindin')
        user3 = User('Ahri')
        user4 = User('Derek')
        user5 = User('Joey')

        user1.add_friend(user2)
        user1.add_friend(user3)
        user1.add_friend(user4)
        user1.add_friend(user5)
        user2.add_friend(user1)
        user3.add_friend(user1)
        user4.add_friend(user1)
        user5.add_friend(user1)

        user1.add_fav_movie('Avengers: Endgame')
        user2.add_fav_movie('Shutter Island')
        user3.add_fav_movie('Shutter Island')
        user4.add_fav_movie('Shutter Island')
        user5.add_fav_movie('Avengers: Endgame')

        popular1 = find_most_popular_movie(user1)
        popular2 = find_most_popular_movie(user2)
        print(f'test_bidirectional_friendships: The most popular movie in {user1.name}\'s network of friends is "{popular1}".')
        print(f'test_bidirectional_friendships: The most popular movie in {user2.name}\'s network of friends is "{popular2}".')
        self.assertEqual(popular1, popular2, f"{user1.name} should have the same most popular favorite movie as {user2.name} because their friend circles exactly overlap.")

    def test_multiple_fav_movies(self):
        user1 = User('Kevin')
        user2 = User('Dindin')
        user3 = User('Ahri')
        user4 = User('Derek')
        user5 = User('Joey')
        user6 = User('Nicole')

        user1.add_friend(user2)
        user1.add_friend(user3)
        user1.add_friend(user4)
        user1.add_friend(user5)
        user2.add_friend(user1)
        user3.add_friend(user1)
        user4.add_friend(user1)
        user5.add_friend(user1)
        user2.add_friend(user6)
        user6.add_friend(user2)

        user1.add_fav_movie('Avengers: Endgame', 'Wolf of Wall Street', 'Whiplash')
        user2.add_fav_movie('Shutter Island', 'Avengers: Infinity War', 'Wolf of Wall Street')
        user3.add_fav_movie('Shutter Island', 'Wolf of Wall Street', 'Fight Club')
        user4.add_fav_movie('Shutter Island', 'Wolf of Wall Street', 'Django Unchained')
        user5.add_fav_movie('Avengers: Endgame', 'Shutter Island', 'Wolf of Wall Street')
        user6.add_fav_movie('Wolf of Wall Street', 'Shutter Island', 'One Piece Film Red')

        popular = find_most_popular_movie(user1)
        print(f'test_multiple_fav_movies: The most popular movie in {user1.name}\'s network of friends is "{popular}".')
        self.assertEqual(popular, 'Wolf of Wall Street', f"{user1.name}'s most popular favorite movie amongst their network should be Wolf of Wall Street.")

    def test_users_outside_of_network(self):
        user1 = User('Kevin')
        user2 = User('Dindin')
        user3 = User('Ahri')
        user4 = User('Derek')
        user5 = User('Joey')
        user6 = User('Nicole')
        user7 = User('Leo')
        user8 = User('Lyndon')

        user1.add_friend(user2)
        user1.add_friend(user3)
        user1.add_friend(user4)
        user1.add_friend(user5)
        user2.add_friend(user1)
        user3.add_friend(user1)
        user4.add_friend(user1)
        user5.add_friend(user1)
        user2.add_friend(user6)
        user6.add_friend(user2)
        user7.add_friend(user8)
        user8.add_friend(user7)

        user1.add_fav_movie('Avengers: Endgame', 'Wolf of Wall Street', 'Whiplash')
        user2.add_fav_movie('Shutter Island', 'Avengers: Infinity War', 'Wolf of Wall Street')
        user3.add_fav_movie('Shutter Island', 'Wolf of Wall Street', 'Fight Club')
        user4.add_fav_movie('Shutter Island', 'Wolf of Wall Street', 'Django Unchained')
        user5.add_fav_movie('Avengers: Endgame', 'Shutter Island', 'Wolf of Wall Street')
        user6.add_fav_movie('Wolf of Wall Street', 'Shutter Island', 'One Piece Film Red')
        user7.add_fav_movie('Shutter Island', 'One Piece Film Red')
        user8.add_fav_movie('Shutter Island', 'Rounders')

        popular1 = find_most_popular_movie(user1)
        popular7 = find_most_popular_movie(user7)
        print(f'test_users_outside_of_network: The most popular movie in {user1.name}\'s network of friends is "{popular1}".')
        print(f'test_users_outside_of_network: The most popular movie in {user7.name}\'s network of friends is "{popular7}".')
        self.assertEqual(popular1, 'Wolf of Wall Street', f"{user1.name}'s most popular favorite movie amongst their network should be Wolf of Wall Street.")
        self.assertEqual(popular7, 'Shutter Island', f"{user7.name}'s most popular favorite movie amongst their network should be Shutter Island.")




if __name__ == "__main__":
    unittest.main()

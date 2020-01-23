import random
import re

class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

        return self.last_id

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        user_ids = []

        alpha = list("abcdefghijklmnopqrstuvwxyz")

        random.shuffle(alpha)

        # Add users
        for i in range(num_users):
            name_range = random.randrange(3, 15)

            user_id = self.add_user("".join(alpha[:name_range]))

            random.shuffle(alpha)
            user_ids.append(user_id)

        # Create friendships
        max_friendships = avg_friendships * 2

        for i in range(num_users):
            friend_count = random.randrange(1, max_friendships)
            friendships_created = 0

            loops = 0

            while friendships_created <= friend_count:
                friend_id = random.randrange(1, num_users)

                temp_i = i + 1

                first =temp_i if temp_i < friend_id else friend_id
                second = friend_id if friend_id > temp_i else temp_i 

                if self.add_friendship(first, second):
                    friendships_created += 1

                loops += 1

                if loops > 10000:
                    break


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.users)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

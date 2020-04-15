import random
import sys
sys.path.append('../graph')
from util import Queue


class User:
    def __init__(self, name):
        self.name = name

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
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

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

        # Add users
        for i in range(num_users):
            name = f'Fake user {i+1}'
            self.add_user(name)
        # Create friendships
        possible_friendships = []
        for i in range(1, num_users+1):
            for j in range(1, num_users+1):
                if i < j:
                    possible_friendships.append((i,j))
        
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue()
        current_path = [user_id]
        while current_path:
            #print('Current path:', current_path)
            current_node = current_path[-1]
            if current_node not in visited:
                visited[current_node] = current_path
                #print(f'New result -- {current_node}: {current_path}')
            for neighbor in self.friendships[current_node]:
                if neighbor not in visited:
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    #print('New path:', new_path)
                    queue.enqueue(new_path)
                    #print('Queue:', queue.queue)
            current_path = queue.dequeue()

        return visited


"""
Answers to questions--

1. QUESTION: To create 100 users with an average of 10 friends each,
how many times would you need to call add_friendship()? Why?

ANSWER: You would need to call it 500 times. In order to give each user
10 friends on average, there need to be 1000 friendships total (1000 / 100 = 10).
However, add_friendship() adds *TWO* friendships each time it's called, since it sets
User B as User A's friend *and also* sets User A as User B's friend. So to get 1000
friendships, we call add_friendship() 500 times.

2. If you create 1000 users with an average of 5 random friends each,
what percentage of other users will be in a particular user's extended social network?
What is the average degree of separation between a user and those in his/her extended network?

Running the code below, I find that the percentage of other users in a social network is about 98.8%,
and the average degree of separation is about 5.46.

3. You might have found the results from question #2 above to be surprising.
Would you expect results like this in real life? If not, what are some ways
you could improve your friendship distribution model for more realistic results?

I wouldn't expect this code in real life. In real life, I assume friendship networks are more
self-contained, so the percentage of other users in one's extended network would be much lower.
(The average degree of separation is less intuitive to me.)

For more realistic results, one method is to pre-divide the ID numbers into groups, and only create
friendships between user IDs in the same group. Or we could keep track of how many users are in
each person's extended network as we add friendships, and refuse to add any more friendships for
that user once they hit a certain number. (This number can be varied from user to user.)
"""

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    #sg.friendships = {1: {8, 7}, 2: {3, 4}, 3: {9, 2}, 4: {8, 2}, 5: {9}, 6: {9}, 7: {8, 9, 1}, 8: {1, 4, 7}, 9: {3, 5, 6, 7}, 10: set()}
    #print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    # Code to answer question #2 above
    friends_means = []
    degree_of_sep_means = []
    for _ in range(10):
        friends_sum = 0
        degree_of_sep_sum = 0
        degree_of_sep_length = 0
        sg.populate_graph(1000, 5)
        for user in range(1, 1001):
            network = sg.get_all_social_paths(user)
            friends_sum += len(network)
            for friend in network.keys():
                degree_of_sep_sum += len(network[friend])
                degree_of_sep_length += 1
        
        friends_means.append(friends_sum / 1000)
        degree_of_sep_means.append(degree_of_sep_sum / degree_of_sep_length)

    avg_friends = sum(friends_means) / 10
    avg_degree_of_sep = sum(degree_of_sep_means) / 10
    print(f'The percentage of other users in the social network is {avg_friends / 10}%.')
    print(f'The average degree of separation is {avg_degree_of_sep}.')
    
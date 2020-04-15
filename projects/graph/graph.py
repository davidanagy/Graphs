"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Check if they exist
        v1_exists = False
        v2_exists = False
        if v1 in self.vertices:
            v1_exists = True
        if v2 in self.vertices:
            v2_exists = True
        # Add the edge
        if v1_exists and v2_exists:
            self.vertices[v1].add(v2)
        else:
            # Raise an error that states which vertex (or vertices) were not found
            if not v1_exists and not v2_exists:
                raise KeyError(f'Vertices {v1} and {v2} not found')
            elif not v1_exists:
                raise KeyError(f'Vertex {v1} not found')
            else:
                raise KeyError(f'Vertex {v2} not found')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # Check if vertex exists
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        # If it doesn't, raise an error
        else:
            raise KeyError(f'Vertex {vertex_id} not found')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Define set of vertices already traversed
        traversed_vertices = {starting_vertex}
        # Create a Queue since it's breadth-first
        queue = Queue()
        current_node = starting_vertex
        # While current_node isn't None
        while current_node:
            print(current_node)
            for neighbor in self.get_neighbors(current_node):
                if neighbor not in traversed_vertices:
                    traversed_vertices.add(neighbor)
                    queue.enqueue(neighbor)
            # Dequeue and set it as current_node.
            # If the queue is empty, current_node will be None
            # and the while-loop will end.
            current_node = queue.dequeue()

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Same as above, just using a Stack instead since it's depth-first.
        traversed_vertices = {starting_vertex}
        stack = Stack()
        current_node = starting_vertex
        while current_node:
            print(current_node)
            for neighbor in self.get_neighbors(current_node):
                if neighbor not in traversed_vertices:
                    traversed_vertices.add(neighbor)
                    stack.push(neighbor)
            current_node = stack.pop()

    # def dft_recursive(self, starting_vertex):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.

    #     This should be done using recursion.
    #     """
    #     traversed_vertices = {starting_vertex}
    #     # Have to create a helper function, or else the
    #     # traversed_vertices set will be overwritten when the
    #     # function is called again.
    #     # The traversed_vertices set is an argument in the helper function.
    #     def recursion_function(vertex, traversed_vertices):
    #         print(vertex)
    #         for neighbor in self.get_neighbors(vertex):
    #             if neighbor not in traversed_vertices:
    #                 traversed_vertices.add(neighbor)
    #                 recursion_function(neighbor, traversed_vertices)
    #     recursion_function(starting_vertex, traversed_vertices)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Initial case
        if visited is None:
            visited = set()

        # Print
        print(starting_vertex)

        # Track visited nodes
        visited.add(starting_vertex)

        # Call the function recursively on neighbors not visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        searched_vertices = {starting_vertex}
        queue = Queue()
        # Similar to a traversal, but instead of
        # queueing values, we're queueing paths.
        # Start at the starting vertex.
        current_path = [starting_vertex]
        while current_path:
            for neighbor in self.get_neighbors(current_path[-1]):
                if neighbor not in searched_vertices:
                    # Create a copy so that we don't interfere with
                    # the original path.
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    if neighbor == destination_vertex:
                        # If we've found the destination, we're done.
                        # Return the path we just made.
                        return new_path
                    else:
                        searched_vertices.add(neighbor)
                        queue.enqueue(new_path)
            current_path = queue.dequeue()
        
        # If the while-loop ends without finding the destination_vertex,
        # that means there's no path from the start to the destination.
        # So return an empty list.
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Same as the above, just using a Stack.
        searched_vertices = {starting_vertex}
        stack = Stack()
        current_path = [starting_vertex]
        while current_path:
            for neighbor in self.get_neighbors(current_path[-1]):
                if neighbor not in searched_vertices:
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    if neighbor == destination_vertex:
                        return new_path
                    else:
                        searched_vertices.add(neighbor)
                        stack.push(new_path)
            current_path = stack.pop()
        
        return None

    # def dfs_recursive(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     traversed_vertices = {starting_vertex}
    #     path = [starting_vertex]
    #     # Again, for similar reasons as the previous recursive function,
    #     # we need a helper function.
    #     # (The print statements below were used for error-checking.)
    #     # Now we need to pass the path through the helper function as well,
    #     # to make sure it's maintained as we call it over and over.
    #     def recursion_function(vertex, destination_vertex, traversed_vertices, path):
    #         #print('Current path:', path)
    #         for neighbor in self.get_neighbors(vertex):
    #             #print('Neighbor:', neighbor)
    #             if neighbor not in traversed_vertices:
    #                 new_path = path.copy()
    #                 new_path.append(neighbor)
    #                 #print('New path:', new_path)
    #                 if neighbor == destination_vertex:
    #                     #print('Destination found')
    #                     return new_path
    #                 else:
    #                     traversed_vertices.add(neighbor)
    #                     search_path = recursion_function(neighbor, destination_vertex,
    #                                                      traversed_vertices, new_path)
    #                     # If "neighbor" has no neighbors (that aren't in traversed_vertices),
    #                     # then "search_path" will be None. We don't want to return a None value.
    #                     # So only return it if it's not None.
    #                     if search_path:
    #                         return search_path

    #     return recursion_function(starting_vertex, destination_vertex,
    #                               traversed_vertices, path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            new_path = list()
        else:
            new_path = path.copy()

        visited.add(starting_vertex)
        new_path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return new_path
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                search_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if search_path:
                    return search_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

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
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print('ERROR ADDING EDGE:  Vertex not found')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print('ERROR:  Vertex not found')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        traversed_vertices = {starting_vertex}
        queue = Queue()
        current_node = starting_vertex
        while current_node:
            print(current_node)
            for neighbor in self.get_neighbors(current_node):
                if neighbor not in traversed_vertices:
                    traversed_vertices.add(neighbor)
                    queue.enqueue(neighbor)
            current_node = queue.dequeue()

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
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

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        traversed_vertices = {starting_vertex}
        def recursion_function(vertex, traversed_vertices):
            print(vertex)
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in traversed_vertices:
                    traversed_vertices.add(neighbor)
                    recursion_function(neighbor, traversed_vertices)
        recursion_function(starting_vertex, traversed_vertices)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        searched_vertices = {starting_vertex}
        queue = Queue()
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
                        queue.enqueue(new_path)
            current_path = queue.dequeue()
        
        return []

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
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

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        traversed_vertices = {starting_vertex}
        path = [starting_vertex]
        def recursion_function(vertex, destination_vertex, traversed_vertices, path):
            #print('Current path:', path)
            for neighbor in self.get_neighbors(vertex):
                #print('Neighbor:', neighbor)
                if neighbor not in traversed_vertices:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    #print('New path:', new_path)
                    if neighbor == destination_vertex:
                        #print('Destination found')
                        return new_path
                    else:
                        traversed_vertices.add(neighbor)
                        search_path = recursion_function(neighbor, destination_vertex,
                                                         traversed_vertices, new_path)
                        if search_path:
                            return search_path

        return recursion_function(starting_vertex, destination_vertex,
                                  traversed_vertices, path)

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

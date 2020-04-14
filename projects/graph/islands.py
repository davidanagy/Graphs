"""
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4
"""
def get_neighbors(matrix, node_x, node_y, size):
    neighbors = []
    if node_y > 0:
        n_neighbor = (node_y-1, node_x)
        neighbors.append(n_neighbor)
    if node_x > 0:
        w_neighbor = (node_y, node_x-1)
        neighbors.append(w_neighbor)
    if node_y < size-1:
        s_neighbor = (node_y+1, node_x)
        neighbors.append(s_neighbor)
    if node_x < size-1:
        e_neighbor = (node_y, node_x+1)
        neighbors.append(e_neighbor)
    return neighbors
    

def dft_traversal_recursive(matrix, node_x, node_y, size, visited):
    neighbors = get_neighbors(matrix, node_x, node_y, size)
    for neighbor in neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            neighbor_x = neighbor[0]
            neighbor_y = neighbor[1]
            if matrix[neighbor_x][neighbor_y] == 1:
                dft_traversal_recursive(matrix, neighbor_x, neighbor_y,
                                        size, visited)


def find_islands(matrix):
    size = len(matrix)
    visited = set()
    islands = 0
    for i in range(size):
        for j in range(size):
            if (i, j) not in visited:
                visited.add((i, j))
                if matrix[i][j] == 1:
                    dft_traversal_recursive(matrix, j, i, size, visited)
                    islands += 1

    return islands

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(find_islands(islands))
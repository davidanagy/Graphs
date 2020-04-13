import sys
sys.path.append('../graph')
from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)
        graph.add_edge(child, parent)
    
    potential_answers = []
    stack = Stack()
    current_path = [starting_node]
    while current_path:
        neighbors = graph.get_neighbors(current_path[-1])
        if len(neighbors) > 0:
            for neighbor in graph.get_neighbors(current_path[-1]):
                new_path = current_path.copy()
                new_path.append(neighbor)
                stack.push(new_path)
        else:
            potential_answers.append(current_path)
        current_path = stack.pop()

    #print('Potential answers:', potential_answers)
    lengths = [len(family_tree) for family_tree in potential_answers]
    max_len = max(lengths)
    if max_len == 1:
        return -1

    new_answers = []
    for i in range(len(lengths)):
        if lengths[i] == max_len:
            new_answers.append(potential_answers[i])

    #print('New answers:', new_answers)
    final_answer = new_answers[0][-1]
    for family_tree in new_answers[1:]:
        answer = family_tree[-1]
        if answer < final_answer:
            final_answer = answer

    return final_answer

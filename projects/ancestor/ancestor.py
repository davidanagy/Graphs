import sys
sys.path.append('../graph')
from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        # Separate out the parent and child
        parent = ancestor[0]
        child = ancestor[1]
        # Add them as vertices if they aren't vertices already
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)
        # Since we're going to be starting at the child and going
        # backwards, we want the child to "point at" the parent.
        # So add the edge with the child first.
        graph.add_edge(child, parent)
    
    # Do a depth-first traversal, adding each full "branch" to the
    # potential_answers list.
    # Because several potential answers could share some of the same vertices,
    # we don't want to keep track of "traversed vertices" like a normal traversal.
    # This is acceptable because it's stated that there are no cycles, so this will
    # never result in an infinite loop.
    potential_answers = []
    stack = Stack()
    # Similar to a search, we'll be pushing and popping paths, not individual nodes.
    current_path = [starting_node]
    while current_path:
        neighbors = graph.get_neighbors(current_path[-1])
        # If there are neighbors, that means the branch is not yet complete,
        # so continue the traversal.
        if neighbors:
            for neighbor in graph.get_neighbors(current_path[-1]):
                new_path = current_path.copy()
                new_path.append(neighbor)
                stack.push(new_path)
        else:
            # If there are no neighbors, we've hit the end of the branch,
            # so append it to potential_answers.
            potential_answers.append(current_path)
        current_path = stack.pop()

    #print('Potential answers:', potential_answers)

    # Now, make a list of the lengths of each branch in potential_answers,
    # and find the max length.
    lengths = [len(family_branch) for family_branch in potential_answers]
    max_len = max(lengths)
    # If the max length is 1, then the traversal ended immediately; i.e.,
    # the individual in question has no parents recorded. So per instructions,
    # return -1.
    if max_len == 1:
        return -1
    # Otherwise, find all the potential answers with length equal to the max length,
    # and append them to "new_answers".
    new_answers = []
    for i in range(len(lengths)):
        if lengths[i] == max_len:
            new_answers.append(potential_answers[i])

    #print('New answers:', new_answers)

    # Finally, check the last value--i.e., the earliest ancestor--in each branch.
    # Per instructions, return the value with the lowest numeric ID.
    final_answer = new_answers[0][-1]
    for family_branch in new_answers[1:]:
        answer = family_branch[-1]
        if answer < final_answer:
            final_answer = answer

    return final_answer

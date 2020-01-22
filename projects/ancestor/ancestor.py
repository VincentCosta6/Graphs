from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        graph.add_edge(pair[1], pair[0])

    print(graph.vertices)

    queue = Queue()
    queue.enqueue( [starting_node] )

    earliest = -1
    max_path = 1

    while queue.size() > 0:
        path = queue.dequeue()
        d = path[-1]

        if (len(path) >= max_path and d < earliest) or (len(path) > max_path):
            print(d)
            max_path = len(path)
            earliest = d
        
        for neighbor in graph.vertices[d]:
            copy = path[:]
            copy.append(neighbor)

            print("do it")
            queue.enqueue(copy)

    print(f"return {earliest}")
    return earliest

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))
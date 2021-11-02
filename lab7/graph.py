# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.


def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    res = []
    with open(file_name, 'r') as file:
        for line in file:
            add = [int(i.strip()) for i in line.split(',')]
            res.append(add)
    return res


def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    res = {}
    for i in edge_list:
        if not i[0] in res:
            res[i[0]] = []
        if not i[1] in res:
            res[i[1]] = []
        res[i[0]].append(i[1])
        res[i[1]].append(i[0])
    for i in res.values():
        i.sort()
    return res


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    return edge[1] in graph[edge[0]]


def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph. 

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if not edge[0] in graph:
        graph[edge[0]] = []
    if not edge[1] in graph:
        graph[edge[1]] = []
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
    return graph


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if not edge[0] in graph[edge[1]]:
        return graph
    graph[edge[0]].remove(edge[1])
    graph[edge[1]].remove(edge[0])
    return graph


def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    graph[node] = graph.get(node, [])
    return graph


def del_node(graph: dict, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if not node in graph:
        return graph
    for i in graph[node]:
        graph[i].remove(node)
    graph.pop(node)
    return graph


def convert_to_dot(graph: dict):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    with open('mygraph.gv', 'w') as file:
        file.write('graph mygraph {\n')
        for i in sorted(graph.keys()):
            for j in graph[i]:
                if j > i:
                    file.write(f'\t{i} -- {j};\n')
        file.write('}')

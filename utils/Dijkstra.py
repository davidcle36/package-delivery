

def dijkstra_shortest_path(g, start_vertex):
    """
    The algorithm computes the shortest path from the initial given vertex to all other
    vertices in the graph. Two data members are required in the vertex are the total distance
    from start to another vertex. Also, reference to the previous vertex.

    The Dijkstra shortest path is somewhat similar as a link list, where one points directly to address,
    and the it is object of an instance. But essentially the same thing. It is like a link list but the link
    carries weight as the vertex connect to its adjacent vertices. As for this program, it is the distance.
    The time complexity of Dijkstra shortest path O(|V| * |E| log |E|) where V is the number of vertices,
    and E is number of edge's weight between vertices. Since the further away from starting point, the greater amount of
    adjacent vertex connect to it, and vice versa. For examples, starting vertex, V, is equal to N vertices
    adjacent to it. For the number of edges, between some vertex_a* and another vertex_b*, an edge must exist,
    and worst case, one travel through all the edges to get to target, O(LogE) times. And in the end, the value
    holding the smallest index is pop, which added E times to the algorithms since it might need to pop the first index
    and then shift the array over by one. Thus making it O(|V| + |E| log |E|)

        But with a hash table, a shifting is not a problem since each items are placed in a bucket. Thus, in the codebase
    for dijkstra_shortest_path time complexity is O(|V| + Log |E|) since the hash function remove smallest index
    takes O(1 + M) or O(1) without the need to shift the list over, and M is  number of collision in the hash table.

    The space complexity is O(|V| + |E|), where V is the number of vertices, and E is the number of edges

    :param g: graph
    :param start_vertex: Vertex
    :return:
    """

    # fill unvisited_queue with adj vertices from vertex
    unvisited_queue = []
    for vertices in g.adjacency_table:
        if len(vertices) != 0:
            for current_vertex in vertices:
                if len(current_vertex) != 0:
                    unvisited_queue.append(current_vertex[0])

    # start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed until the list is empty.
    # O(E + V log V)
    while len(unvisited_queue) > 0:
        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_table.get(current_vertex):
            edge_weight = g.edge_weights_table.get((current_vertex, adj_vertex))
            alternative_path_distance = current_vertex.distance + edge_weight

            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.prev_vertex = current_vertex


def get_shortest_path(start_vertex, end_vertex, edge_weights):
    """
    Print shortest paths sorted by Dijkstra algorithm

    :param start_vertex: String
    :param end_vertex:  String
    :param edge_weights: Float
    :return: [String, Float]
    """
    cur_vertex = end_vertex
    path = []
    distance = 0.0

    if end_vertex.label == "HUB":
        cur_vertex = start_vertex
        while cur_vertex.label is not None and cur_vertex.prev_vertex is not None:
            distance += edge_weights.get((cur_vertex, cur_vertex.prev_vertex))
            path.insert(-1, cur_vertex.label)
            cur_vertex = cur_vertex.prev_vertex

        path.append(end_vertex.label)
        return [path, distance]
    else:
        while cur_vertex is not None and cur_vertex.prev_vertex is not None:
            if cur_vertex.label in path or start_vertex is cur_vertex:
                break
            distance += edge_weights.get((cur_vertex, cur_vertex.prev_vertex))
            path.insert(0, cur_vertex.label)
            cur_vertex = cur_vertex.prev_vertex

        path.insert(0, start_vertex.label)

        return [path, distance]

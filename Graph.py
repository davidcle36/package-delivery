from utils.HashMap2 import HashMap
from utils.Dijkstra import dijkstra_shortest_path, get_shortest_path


class Vertex:
    """
    A node with weighted edges that connect two nodes.
    Dijkstra's shortest path algorithm utilize a pointer to point to
    its predecessor point prev_vertex and distance to find shortest path.
    """

    def __init__(self, label, edges):
        """

        :param label:String
        :param edges: [ float ]
        """
        self.label = label
        self.edges = edges
        self.distance = float('inf')
        self.prev_vertex = None

    def __repr__(self):
        return "Vertex: " + self.label


class Graph:
    """
        A Graph is a data structure that is composed of vertices and each vertices are connected to its adjacent vertices.
    This type of graph, in which vertices are connected by edges, is called a weighted or undirected graph.

        Graph has a adjacency list table, each vertex has list of adjacent vertices, with each list item representing an edge
    Also edge weights table to get the value from some vertex to another vertex using a tuple as a key to get value.

        V = number of Vertices, E = number of Edges, P = number of packages.


        Space complexity: O(V + E)
    """

    def __init__(self):
        self.adjacency_table = HashMap(40)
        self.edge_weights_table = HashMap(500)

    def add_vertex(self, new_vertex):
        """
        Add new vertex to graph.

            Time Complexity: O(V)


        :param new_vertex: Vertex
        :return:
        """
        self.adjacency_table.add(new_vertex, [])

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        """
        Add directed edge from from_vertex to to_vertex along with the distance between them.

            To get the from_vertex from adjacency_table, a search time of
        O(1) is needed.

            From the value between from_vertex and to_vertex, it needs to be added to edge_weights table. The
         time complexity to add is O(E)

            Lastly, updating adjacency_table that points to from_vertex and the values are adjacent
        vertices. It takes O(N) to update table.

            Therefore, total time complexity:
                1 + E + V = O(E + V)


        :param from_vertex: Vertex
        :param to_vertex: Vertex
        :param weight: float
        :return:
        """

        # O(1)
        new_from_vertex = self.adjacency_table.get(from_vertex)
        new_from_vertex[len(new_from_vertex):] = [to_vertex]

        # O(E)
        self.edge_weights_table.add((from_vertex, to_vertex), weight)

        # O(V)
        self.adjacency_table.update(from_vertex, new_from_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        """
            An undirected_edge includes in weight between one point and another.
        The reason for adding flipped vertices is for reversing from point b to point.

            Total time complexity: O(E + V)

        :param vertex_a: String
        :param vertex_b: String
        :param weight: float
        :return:
        """

        # O(E + V)
        self.add_directed_edge(vertex_a, vertex_b, weight)

        # O(E + V)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def get_vertex(self, address):
        """
            Search for vertex that match address.

            Time Complexity: O(V^2)

        :param address: String
        :return: Vertex
        """

        # V * V = O(V^2)
        for v in self.adjacency_table:
            if len(v) != 0:
                # O(V)
                for vertex in v:
                    if vertex[0].label == address:
                        return vertex[0]

    def Build_Undirected_Graph(self, packages):
        """
            Taking an undirected graph and the packages to be sent to its address, build_undirected
        graph, in a sense, builds a map with edge's weights.

            The outcome is to have an weighted graph with all possible vertices path routed from one to another
        vertex, so it has to loop through all known vertices and find a match with the address that is being sent. And t
        hat address many possible route to get to and from that destination. This function is highly extensive given
        a larger V, E.

            Time complexity: O(V^2E + V^3))
        ,

        :param packages:[ Package ]
        :return:
        """

        # V(V * (1 + 2E + V)) = O(V^2E + V^3))
        for vertices in self.adjacency_table:
            if len(vertices) != 0:
                # V * (1 + 2E + V) = O(VE + V^2))
                for vertex in vertices:
                    # 1 + 2E + V = O(E + V)
                    for idx, edge in enumerate(vertex[0].edges):
                        if edge:
                            # O(1)
                            vertex_b = self.get_vertex(packages[idx].location)

                            # O(E + V))
                            self.add_undirected_edge(vertex[0], vertex_b, edge)

    def Draw_Path(self, start, end):
        """
            Method to get to route taken and distance from start
        to end.

            Time Complexity: V + E = O(V + E)

        :param start: String
        :param end: String
        :return: [ [path:String] , distance:Integer ]
        """
        try:
            vertex_a = self.get_vertex(start)
            dijkstra_shortest_path(self, vertex_a)
            datum = [[], 0.0]
            for vertices in self.adjacency_table:
                if len(vertices) != 0:
                    for vertex in vertices:
                        if vertex[0] is None and vertex[0] is not vertex_a:
                            continue
                        else:
                            if vertex[0].label == end:
                                datum = get_shortest_path(vertex_a, vertex[0], self.edge_weights_table)
            return datum
        except Exception as e:
            print("Error: ", e)
            return datum



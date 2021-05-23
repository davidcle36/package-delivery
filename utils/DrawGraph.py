from Graph import Vertex
from utils.Dijkstra import dijkstra_shortest_path, get_shortest_path


# def Build_Undirected_Graph(a_list, graph):
#     for vertices in graph.adjacency_list:
#         if len(vertices) != 0:
#             for vertex in vertices:
#                 for idx, edge in enumerate(vertex[0].edges):
#                     if edge:
#                         vertex_b = graph.get_vertex(a_list[idx].location)
#                         graph.add_undirected_edge(vertex[0], vertex_b, edge)


# def Draw_Path(graph, start, end):
#     try:
#         vertex_a = graph.get_vertex(start)
#         dijkstra_shortest_path(graph, vertex_a)
#         datum = [[], 0.0]
#         for vertices in graph.adjacency_list:
#             if len(vertices) != 0:
#                 for vertex in vertices:
#                     if vertex[0] is None and vertex[0] is not vertex_a:
#                         continue
#                     else:
#                         if vertex[0].label == end:
#                             datum = get_shortest_path(vertex_a, vertex[0], graph.edge_weights)
#         return datum
#     except Exception as e:
#         print("Error: ", e)
#         return datum

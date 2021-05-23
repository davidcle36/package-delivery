#       Name: David Le
# Student ID: 001515101

from datetime import datetime

from Graph import Graph, Vertex
from view.Menu import Menu
from utils.DataLoader import LoadPackageData, LoadDistanceData
from utils.HashMap2 import HashMap
from utils.lists_remove_merged_duplicates import lists_remove_merged_duplicates
from model.Truck import Truck

"""
B.  Write an overview of your program, in which you do the following:
    
    B.1 Explain the algorithm’s logic using pseudocode.
    ---------------------------------------------------
    
        The algorithm comprise three components, the data structure, sorting and 
        then traversal.

        Graph Data Structure:
        
               After a Hash Table has been built for each location and the respective miles as vertex. Then when added to graph, each
            vertex has a label, and a list of miles from that vertex to others. Knowing the distance between
            point A to point B, a weighted(undirected) graph can be created.

            #######
            #
            # File: /Graph.py, /utils.DrawGraph
            #
            # Classes: Graph, Vertex
            #
            #
            ######

            Building an undirected graph:
                Class: Graph

                    Using a hash table, with the key being the address, and the values
                    being the edge's weight between it and the many vetices. It provides the
                    time complexity of O(1) when searching, or updated by address.

                    Another hash table that is initialize is edge_weights, which holds the value of between two points given
                    the time complexity of O(1) when searching (address A, address B).

                    The time complexity to build undirected graph is N + (N * N) = O(N * N)
                    The space complexity is O(V + E) where V are the vertices and E are the edge's weights

                        
                    Pseudocode: 
                    ################################

                    def Build_Graph(self):
                        locations = [...Location]
                        adjacency_list = HashMap(S) // S is number of locations
                        edge_weights = HashMap(M)   // M is the number pair of vertex

                        For each Location in locations:
                            Add Vertex to adjacency_list

                        i += 1
                        For each vertex_a in adjacency_list:
                            while i < len(adjacency_list):
                              if edge:
                                vertex_b = adjacency_list.get(key of adjacency_list i)      // O(1)
                                edge_weights.insert((vertex_a, vertex_b), vertex_b.weight)  // O(1)
                                edge_weights.insert((vertex_b, vertex_a), vertex_b.weight)  // O(1)
                                adjacency_list.update(vertex_a, [from vertex_a : to vertices adjacent of vertex_a, 
                                    vertex_b -> vertex_N*]) // O(1 + K), where K is the number of collision
                                adjacency_list.update(vertex_b, [from vertex_b : to vertices adjacent of vertex_b, 
                                    vertex_a -> vertex_N*]) // O(1 + K), where K is the number of collision
                            i += 1

                    ################################
                                    
                                 
                    Class Graph's Methods
                    -----------------------------
                    Add_Vertex(self, String address, [] adjacent miles of address)
                        Time Complexity: O(N)

                        Pseudocode:
                        ##############################

                        ...
                        For each Location in locations:
                            Add Vertex to adjacency_list
                        ...

                        ##############################

                        

                    Add_Undirected_Edge(self)
                        Input: vertex A, Vertex B that is adjacent to A, and the edge weight between them
                        Time Complexity: 5(1) * N * N = O(N * N)
                        
                        Pseudocode:
                        ##############################

                        ...
                        For each vertex_a in adjacency_list:    // O(N)
                            while i < len(adjacency_list):      // O(N)
                              if edge:
                                vertex_b = adjacency_list.get(key of adjacency_list i)      // O(1)
                                edge_weights.insert((vertex_a, vertex_b), vertex_b.weight)  // O(1)
                                edge_weights.insert((vertex_b, vertex_a), vertex_b.weight)  // O(1)
                                adjacency_list.update(vertex_a, [from vertex_a : to vertices adjacent of vertex_a, 
                                    vertex_b -> vertex_N*]) // O(1 + K), where K is the number of collision
                                adjacency_list.update(vertex_b, [from vertex_b : to vertices adjacent of vertex_b, 
                                    vertex_a -> vertex_N*]) // O(1 + K), where K is the number of collision
                        ...

                        ##############################
                        
                
        Dijkstra's shortest path algorithm:
            
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
            
            
            Pseudocode
            ################################
                
                def dijkstra_shortest_path(Graph graph, Vertex vertex_a):
                    unvisited_queue = []
                    
                    
                    # Placed all locations in the unvisited_queue[]
                    # Time Complexity is O(N*N)
                    
                    for each vertices in locations[0 -> N]:
                        for each vertex in vertices:
                            if vertex.adjacent[0 -> N] is not None:
                                Add vertex to unvisited Queue
                                
                    Set the distance of starting vertex = 0
                    
                    # Find the smallest distance between between vertex_a and another vertex.
                    # Linked the found vertex to the previous vertex
                    # 
                    # It works similar to a linked list as each vertex has a previous vertex,
                    # and the head previous is none, which conclude the route. So from the last
                    # of the list, it is possible to trace back to the beginning.
                    #
                    # Example: 
                    #       3th st -> 2nd st -> 1st st -> None, when 1st st is the starting point.
            
                    while unvisited_queue is not empty:
                        smallest_index = 0
                        for each item in unvisited_queue[0 -> N]:
                            if item.distance < item[smallest_index].distance then
                                smallest index = indexOf(item)
                        current_vertex = unvisited_queue.pop(smallest_index)
                    
                    
                        for each adjacent vertex from current_vertex:
                            weight = from current to adj vertex
                            total_distance_between = current distance + weight
                            
                            if short path is found from current to another adjacent vertex:
                                adj distance = total_distance_between
                                adj vertex -> prev = current vertex
                                
            ################################
            
            
        
            

        Edge's Weight Comparison Sorting:
            
                After building an undirected graph, a method can be used to compared the distance between
            vertex_a and vertex_b to find the minimum with Dijkstra and break them into list of package ids. The package ids
            would call a getter to get in instance of that Package, thus, getting the address, notes, time, etc.
            
                For the Edge's weight comparison, the codebase would use two package addresses to get the distance 
            between them from the hash table, Graph.edge_weights. The key to search for the distance between the vertex 
            is a tuple(vertex_a, vertex_b), which was already set up when the undirected graph was built. Since the
            max packages per truck, the sorted route list will be at max 16.
            
            The Time complexity is O(N^3 * log |E|)
            The space complexity is O(V + E)
            
            * As I was having problem sorting it, I have to manually count how much packages a truck can get at a time,
              and the special notes condition as much as I could without going over 140 miles while fulfilling deadline.
                    
            ** B.2 Detailed description, and how space and time complexity was arrived in /Truck.py
            
                Pseudocode:
                ################################
                
                def sort_by_distance(self, HashMap hash_table_package, String packages_ids[], 
                                        int max_load_in_truck)
                    packages_in_truck = []
                    min_weight = float("inf") 
                    current_address = "HUB" 
                    end_address = ""
                    picked_package = ""
              
                    # Loop through the entire packages and get every possible weight between two vertices and return only
                    # the shortest path v1 <--> v2 <--> v2 ... vN <--> vN - 1 through dijkstra_shortest_path algorithm
              
                    while i < length of package_ids[]:    
                        dijkstra_shortest_path(graph, hash_table_package[vertex_a])
                        weight = float("inf")
                                         
                        # For each vertex, get the minimum between starting vertex_a and vertex_K, where k 
                        # can be vertex 1 to N                 
                                            
                        for each vertices in adjacency_list:
                            for each current_vertex in vertices:
                                if current_vertex is vertex_a:
                                    weight = Dijkstra's shortest path between current and vertex a
                                                 
                        if weight < min_weight 
                                and package_id not in packages_in_truck 
                                and packages_in_truck < max_load_in_truck:
                            min_weight = weight[i]
                            end_address = vertex_b address
                            picked_package = packages_ids[i]
                                
                        Add picked_package to packages_in_truck
                        current_address = end_address
                        i++
                        
                    return packages_in_truck
                                 
                def sort_packages(self, HashMap hash_table_package , String package_ids[]): 
                    max_load_in_truck = single value from 1 -> N When N is less than or equal to 16
                

                    packages_in_truck = sort_by_distance(self, hash_table_package, package_ids, length(packages_ids))
                    sorted_packages_in_truck_Trip_1 = sort_by_distance(self, hash_table_package, 
                                                                    package_ids[0 -> max_load_in_truck], max_load_in_truck)
                                                                    
                    leftover_packages = packages_in_truck[] - sorted_packages_in_truck_Trip_1[]
                    ...
                    
                    sorted_packages in truck_Trip_N = ...                                                
                                                                   
                                                                    
                    return sorted_packages_in_truck_trip (1 -> N)
        
        Conclusion of B.1 ------------------------------------- -------------------------------------           
"""

# Create a list of Class, Package from /data/package.csv
package_list = LoadPackageData('./data/package.csv')

# Create a list of Class, Distance from /data/distance.csv
distance_list = LoadDistanceData('./data/distance.csv')

# Initialize Hashmap based on size of list, package_list
hash_package = HashMap(len(package_list))

# Initialize Hashmap based on size of list, package_list
hash_path = HashMap(len(distance_list))

# Initialize an instance of Graph.
graph = Graph()

# Initialize an instance of a truck along with the time it will start leaving the Hub.
truck_1 = Truck(1, datetime.strptime("08:00", "%H:%M"))
truck_2 = Truck(2, datetime.strptime("09:05", "%H:%M"))

if __name__ == '__main__':

    # For each package in package list, add the Class, Package
    # to the hashmap, hash_package
    for package in package_list:
        hash_package.add(package.id, package)

    # For each distances in distance list, add the Class, Distance
    # to the hashmap, hash_distance
    for distance in distance_list:
        hash_path.add(distance.location, [float(i) for i in distance.paths[:distance.size]])

    for distance in distance_list:
        graph.add_vertex(Vertex(distance.location, list(distance.paths)))

    plist = []

    for p in package_list:
        plist.append(p.id)

    graph.Build_Undirected_Graph(distance_list)

    # first_route = truck_1.sort_packages(graph, hash_package, plist)
    # log1 = truck_1.start_delivery(graph, hash_package, first_route)
    #
    # plist2 = lists_remove_merged_duplicates(plist, first_route)
    # second_route = truck_2.sort_packages_second(graph, hash_package, plist2)
    # log2 = truck_2.start_delivery(graph, hash_package, second_route)
    #
    # plist3 = lists_remove_merged_duplicates(plist2, second_route)
    # third_route = truck_1.sort_packages_third(graph, hash_package, plist3)
    # log3 = truck_1.start_delivery(graph, hash_package, third_route)
    #
    # plist4 = lists_remove_merged_duplicates(plist3, third_route)
    # fourth_route = truck_2.sort_packages_fourth(graph, hash_package, plist4)
    # log4 = truck_2.start_delivery(graph, hash_package, fourth_route)
    #
    # total_distance = truck_1.get_total_distance() + truck_2.get_total_distance()
    # total_time_elapse = (truck_1.get_total_time() / 60) + (truck_2.get_total_time() / 60)

    first_route = truck_1.chuck_and_sort_packages(graph, hash_package, plist, 1)
    log1 = truck_1.start_delivery(graph, hash_package, first_route)

    plist2 = lists_remove_merged_duplicates(plist, first_route)
    second_route = truck_2.chuck_and_sort_packages(graph, hash_package, plist2, 2)
    log2 = truck_2.start_delivery(graph, hash_package, second_route)

    plist3 = lists_remove_merged_duplicates(plist2, second_route)
    third_route = truck_1.chuck_and_sort_packages(graph, hash_package, plist3, 3)
    log3 = truck_1.start_delivery(graph, hash_package, third_route)

    plist4 = lists_remove_merged_duplicates(plist3, third_route)
    fourth_route = truck_2.chuck_and_sort_packages(graph, hash_package, plist4, 4)
    log4 = truck_2.start_delivery(graph, hash_package, fourth_route)

    full_route = log1 + log2 + log3 + log4

    Menu(truck_1, truck_2, hash_package, [first_route, second_route, third_route, fourth_route], package_list, full_route).main_menu()


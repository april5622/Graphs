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
        # create the new key with the vertex id, and set the value to an empty set (meaning no edges)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex V1 in our vertices, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting_vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create an empty set to track visited vertices
        visited_vertices = set()

        # while the queue is not empty:
        while queue.size() > 0:
            # get current vertex (dequeue from queue)
            current_vertex = queue.dequeue()
            
            # Check if the current vertex has not been visited
            if current_vertex not in visited_vertices:
                visited_vertices.add(current_vertex)
                # print the current vertex
                print(current_vertex)
                # Mark the current vertex as visited
                neighbor_vertex = self.get_neighbors(current_vertex)
                for neighbor in neighbor_vertex:
                    # Add the current vertex to a visited_set
                    queue.enqueue(neighbor)
                
            # Queue up all the current vertex's neighbors (so we can visit them next)
         

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting_vertex
        stack = Stack()
        stack.push(starting_vertex)
        # Create an empty set to track visited vertices
        visited_vertices = set()

        # while the queue is not empty:
        while stack.size() > 0:
            # get current vertex (pop from stack)
            current_vertex = stack.pop()
        
            # Check if the current vertex has not been visited
            if current_vertex not in visited_vertices:
                visited_vertices.add(current_vertex)
                # print the current vertex
                print(current_vertex)
                # Mark the current vertex as visited
                neighbor_vertex = self.get_neighbors(current_vertex)
                for neighbor in neighbor_vertex:
                    # Add the current vertex to a visited_set
                    stack.push(neighbor)
                
            # Push up all the current vertex's neighbors (so we can visit them next)

  

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        # for each neighbor, recurse this function with an updated visited set
        for child_vertex in self.vertices[starting_vertex]:
            if child_vertex not in visited:
                self.dft_recursive(child_vertex, visited)
                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue the starting_vertex
        queue = Queue()
        visited_vertices = set()
        # Create an empty set to track visited vertices
        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        # while the queue is not empty:
        while queue.size() > 0:
            # get current vertex PATH (dequeue from queue)
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']
            # set the current vertex to the LAST element of the PATH

            # Check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:

                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                # IF IT IS, STOP AND RETURN
                if current_vertex == destination_vertex:
                    return current_path

                # Mark the current vertex as visited
                # Add the current vertex to a visited_set
                visited_vertices.add(current_vertex)

                for neighbor_vertex in self.get_neighbors(current_vertex):
                # Queue up NEW paths with each neighbor:
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)

                    queue.enqueue({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited_vertices = set()
        # Create an empty set to track visited verticies
        stack.push({ 
            'current_vertex': starting_vertex,
            'path': [starting_vertex]        
        })
        # while the queue is not empty:
        while stack.size() > 0:
            # get current vertex PATH (dequeue from queue)
            current_obj = stack.pop()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']
            # set the current vertex to the LAST element of the PATH

            # Check if the current vertex has not been visited:
            if current_vertex not in visited_vertices:

                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                # IF IT IS, STOP AND RETURN
                if current_vertex == destination_vertex:
                    return current_path

                # Mark the current vertex as visited
                # Add the current vertex to a visited_set
                visited_vertices.add(current_vertex)

                for neighbor_vertex in self.get_neighbors(current_vertex):
                # Queue up NEW paths with each neighbor:
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    stack.push({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })
        return None


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # REFERENCE DFT_RECRUSIVE FOR A "SIMPLER" ALGORITHM
        if visited is None:
            visited = set()
        # This is like DFT, but we extend the function even further by adding an optional path variable to keep building a path
        # With recursion, if you ever need to "build" as you recurse, think "extra variable"
        if path is None:
            path = []

        visited.add(starting_vertex)
        # Handle updating the current path here
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        # for each neighbor, recurse this function with an updated visited set and an updated path
        for child_vert in self.get_neighbors(starting_vertex):
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None

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

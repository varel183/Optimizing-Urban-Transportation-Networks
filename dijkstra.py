import heapq
import matplotlib
matplotlib.use('TkAgg') 
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.vertexNameArray = []  
        self.vertexIndexMap = {}  
        self.vertexPositionArray = []  
        self.edgeArray = []  

    # Add a new vertex with its name and position
    def addVertex(self, name, x, y):
        self.vertexIndexMap[name] = self.vCount()  
        self.vertexNameArray.append(name)  
        self.vertexPositionArray.append((x, y))  

    # Add a directed edge with a weight between two vertices
    def addEdge(self, vName1, vName2, weight):
        self.edgeArray.append((self.vertexIndexMap[vName1], self.vertexIndexMap[vName2], weight))

    # Return the current count of vertices
    def vCount(self):
        return len(self.vertexNameArray)

    # Return the current count of edges
    def eCount(self):
        return len(self.edgeArray)

    # Find the weight of an edge between two vertices (if it exists)
    def weight_between(self, x, y):
        for edge in self.edgeArray:
            if self.vertexNameArray[edge[0]] == x and self.vertexNameArray[edge[1]] == y:
                return edge[2]
        return None 

    # Find all adjacent vertices of a given vertex
    def find_adjacent(self, u):
        result = []
        for edge in self.edgeArray:
            if edge[0] == self.vertexIndexMap[u]:
                result.append(self.vertexNameArray[edge[1]])
        return result

    # Implement Dijkstra's algorithm for shortest path
    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertexIndexMap}  
        distances[start] = 0 
        previous = {vertex: None for vertex in self.vertexIndexMap}  
        
        pq = [(0, start)]  
        heapq.heapify(pq)  
        
        states = [] 

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)  

            # Skip if this distance is already outdated
            if current_distance > distances[current_vertex]:
                continue
            
            # Save the current state of distances for later reference
            states.append(dict(distances))

            # Relax edges for all neighbors of the current vertex
            for neighbor in self.find_adjacent(current_vertex):
                edge_weight = self.weight_between(current_vertex, neighbor)
                if edge_weight is not None:
                    distance = current_distance + edge_weight

                    # Update the distance if a shorter path is found
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous[neighbor] = current_vertex
                        heapq.heappush(pq, (distance, neighbor))  
                        
        states.append(dict(distances))  
        
        return distances, previous, states  

    # Draw the graph using NetworkX and Matplotlib
    def draw_graph(self):
        G = nx.DiGraph() 
        
        # Add vertices with positions
        pos = {}
        for i, (name, (x, y)) in enumerate(zip(self.vertexNameArray, self.vertexPositionArray)):
            G.add_node(name)
            pos[name] = (x, y)
        
        # Add edges with weights
        for edge in self.edgeArray:
            v1 = self.vertexNameArray[edge[0]]
            v2 = self.vertexNameArray[edge[1]]
            weight = edge[2]
            G.add_edge(v1, v2, weight=weight)
        
        # Draw the graph
        plt.figure(figsize=(10, 7)) 
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', arrowsize=20)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
        plt.title("Graph Visualization")  
        plt.show() 

# Testing the implementation
def test_graph_visualization():
    g = Graph()
    
    # Add vertices
    g.addVertex('s', 0, 0)
    g.addVertex('t', 1, 0)
    g.addVertex('x', 2, 0)
    g.addVertex('y', 1, 1)
    g.addVertex('z', 2, 1)
    
    # Add edges with weights
    g.addEdge('s', 't', 10)
    g.addEdge('s', 'y', 5)
    g.addEdge('t', 'x', 1)
    g.addEdge('t', 'y', 2)
    g.addEdge('y', 't', 3)
    g.addEdge('y', 'x', 9)
    g.addEdge('y', 'z', 2)
    g.addEdge('z', 'x', 4)
    g.addEdge('x', 'z', 6)
    
    # Run Dijkstra's algorithm
    distances, previous, states = g.dijkstra('s')
    print("Distances:", distances)
    print("Previous vertices:", previous)
    
    # Visualize the graph
    g.draw_graph()

if __name__ == "__main__":
    test_graph_visualization()

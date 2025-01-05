# Optimizing Urban Transportation Networks: Comparative Analysis of Dijkstra's Algorithm in Graph-Based Shortest Path Solutions

This project implements a graph data structure and uses Dijkstra's algorithm to find the shortest path between nodes in a directed weighted graph. The graph is visualized using the `NetworkX` library in Python.

Paper : [Optimizing Urban Transportation Networks: Comparative Analysis of Dijkstra's Algorithm in Graph-Based Shortest Path Solutions](https://drive.google.com/file/d/10-32bzp5EdYUK66CYouRoDykO8ZZFq4E/view?usp=sharing)

Video : [Youtube Video](https://youtu.be/W233D2MKjcw)


## Features
- Add vertices with custom positions.
- Add directed edges with weights between vertices.
- Perform Dijkstra's algorithm to find the shortest paths from a given source vertex.
- Visualize the graph using `Matplotlib` and `NetworkX`.

## Requirements
- Python 3.x
- `heapq` (built-in Python module)
- `matplotlib` (for graph visualization)
- `networkx` (for graph creation and visualization)

You can install the required external libraries using `pip`:

```bash
pip install matplotlib networkx
```

## Class: `Graph`

The `Graph` class represents a directed graph and provides the following methods:

### `__init__(self)`
Initializes the graph with empty lists for vertices and edges.

### `addVertex(self, name, x, y)`
Adds a vertex with a specified name and position (`x`, `y`).

### `addEdge(self, vName1, vName2, weight)`
Adds a directed edge between two vertices with a given weight.

### `vCount(self)`
Returns the current count of vertices in the graph.

### `eCount(self)`
Returns the current count of edges in the graph.

### `weight_between(self, x, y)`
Returns the weight of an edge between two vertices (`x` and `y`), or `None` if the edge doesn't exist.

### `find_adjacent(self, u)`
Returns a list of vertices adjacent to vertex `u`.

### `dijkstra(self, start)`
Performs Dijkstra's algorithm to calculate the shortest path from the `start` vertex to all other vertices. Returns the distances, previous vertices, and the states of the algorithm during its execution.

### `draw_graph(self)`
Visualizes the graph using `NetworkX` and `Matplotlib`. The graph is displayed with vertex names and edge weights.

## Testing the Implementation

The `test_graph_visualization()` function demonstrates how to use the `Graph` class.

1. It adds vertices and edges to the graph.
2. It runs Dijkstra's algorithm starting from vertex `'s'`.
3. It prints the distances and previous vertices from the source vertex.
4. It visualizes the graph using `Matplotlib`.

### Example Output:

```bash
Distances: {'s': 0, 't': 8, 'x': 9, 'y': 5, 'z': 7}
Previous vertices: {'s': None, 't': 'y', 'x': 't', 'y': 's', 'z': 'y'}
```

### Graph Visualization:

The graph will be displayed in a new window with vertex labels and edge weights.

## How to Run

1. Clone this repository or download the code file.
2. Run the script using Python:

```bash
python dijkstra.py 
```

This will run the Dijkstra algorithm and display the graph visualization.


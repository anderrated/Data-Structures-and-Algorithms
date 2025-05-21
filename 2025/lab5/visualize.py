import networkx as nx
import matplotlib.pyplot as plt

# Adjacency list
adj = [[1, 2], [0, 2, 3], [0, 4], [1, 4], [2, 3]]

# Create an empty graph
G = nx.Graph()

# Add edges from the adjacency list
for i, neighbors in enumerate(adj):
    for neighbor in neighbors:
        G.add_edge(i, neighbor)

# Draw the graph
pos = nx.spring_layout(G)  # Positions nodes for a nice layout
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=16)
plt.title("Graph Visualization from Adjacency List")
plt.show()

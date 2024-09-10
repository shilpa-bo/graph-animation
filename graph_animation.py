import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import matplotlib.animation as animation

# Create a graph using networkx
G = nx.Graph()

# Add nodes and edges to create a tree structure
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'G'), ('G', 'D'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F')
])

# Assign each node to a layer (partition) manually
# For example, 'A' is at level 0, 'B' and 'C' are at level 1, and so on
for node, layer in [('A', 0), ('B', 1), ('C', 1), ('G', 1), ('D', 2), ('E', 2), ('F', 2)]:
    G.nodes[node]['layer'] = layer

# Use the multipartite layout
pos = nx.multipartite_layout(G, subset_key='layer')

# BFS function that tracks node discovery order
def bfs_animation(G, start_node):
    visited = set()
    queue = deque([start_node])
    node_order = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            node_order.append(node)
            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)
    return node_order

# Animate the BFS traversal
def animate_bfs(i):
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=15)
    if i < len(node_order):
        node = node_order[i]
        # Highlight the currently visited node
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='orange', node_size=600)
    if i > 0:
        # Highlight the path up to the current node
        nx.draw_networkx_nodes(G, pos, nodelist=node_order[:i], node_color='lightgreen', node_size=600)

# Set up the figure and axis for plotting
fig, ax = plt.subplots()

# Get the BFS node discovery order
node_order = bfs_animation(G, 'A')

# Create the animation
ani = animation.FuncAnimation(fig, animate_bfs, frames=len(node_order) + 2, interval=1000, repeat=False)

# Show the animation
plt.show()

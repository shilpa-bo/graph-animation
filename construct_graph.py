import networkx as nx
import matplotlib.pyplot as plt

class Node:
	def __init__(self, value):
		"""
		node for a graph, has a value and neighbor list
		"""
		self.value = value
		self.neighbors = []
class Graph:
	def __init__(self):
		"""
		constructing graph with node class
		calling Graph() sets up an empty dictionary to store the nodes 
		graph has no nodes or edges, just an empty container to store the dictionary
		allows quick access to nodes based on their values, can lookup nodes in O(1) time
		"""
		self.nodes = {}

	def add_node(self, value):
		"""
		adds a node to the graph
		"""
		if value not in self.nodes:
			self.nodes[value] = Node(value)
		return self.nodes[value]
		
	
	def add_edge(self, value1, value2, bidirectional=True):
		"""
		adds an edge between two nodes in graph
		"""
		if value1 not in self.nodes:
			self.add_node(value1)
		if value2 not in self.nodes:
			self.add_node(value2)
		node1 = self.nodes[value1]
		node2 = self.nodes[value2]
		self.nodes[value1].neighbors.append(node2)
		if bidirectional:
			self.nodes[value2].neighbors.append(node1)
	def remove_node(self,value):
		"""
		removes node from graph and removes it from any neighbor lists
		"""
		if value in self.nodes:
			node_to_remove = self.nodes[value]
			for node in self.nodes.values():
				if node_to_remove in node.neighbors:
					node.neighbors.remove(node_to_remove)
			del self.nodes[value]
		else:
			print(f"{value} not in graph")
	def remove_edge(self, value1, value2, bidirectional):
		"""
		removes edge between 2 nodes from graph, and removes it from any neighbor lists
		"""
		if value1 in self.nodes and value2 in self.nodes:
			node1 = self.nodes[value1]
			node2 = self.nodes[value2]
			if node2 in node1.neighbors:
				node1.neighbors.remove(node2)
			if bidirectional and node1 in node2.neighbors:
				node2.neighbors.remove(node1)
		else:
			print("One or two of the nodes are not found")
	def get_node(self, value):
		"""
		returns a node object corresponding to the value
		if value doesn't exist, then return None as default
		"""
		return self.nodes.get(value, None)
	def display(self):
		"""
		returns a simple graph representation of all nodes in the graph along with its neighbors
		"""
		graph = self.nodes
		for node in graph.values():
			neighbors = [neighbor.value for neighbor in node.neighbors]
			print(f"{node.value}: {neighbors}")
	def dfs_it(self, root):
		"""
		traverses graph using DFS iterativelu
		"""
		stack = [root]
		visited = []
		while stack:
			curr = stack.pop()
			visited.append(curr.value)
			for neighbor in reversed(curr.neighbors):
				if neighbor.value not in visited:
					stack.append(neighbor)
		return visited

	def dfs(self,root):
		"""
		traverses graph using DFS recursively
		"""
		
	def bfs(self, root):
		"""
		traverses graph using BFS
		"""
		stack = [root]
		visited = []
		while stack:
			curr = stack.pop(0)
			visited.append(curr.value)
			for neighbor in curr.neighbors:
				if neighbor.value not in visited:
					stack.append(neighbor)
		return visited

	
	def visualize(self):
		"""
		Visualizes the graph using NetworkX and Matplotlib.
		"""
		G = nx.Graph()  # Create a graph object using NetworkX

		# Add nodes and edges to the NetworkX graph
		for node in self.nodes.values():
			G.add_node(node.value)
			for neighbor in node.neighbors:
				G.add_edge(node.value, neighbor.value)

		# Draw the graph
		pos = nx.spring_layout(G)  # Positions the nodes for a visually appealing layout
		nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15, font_color='black', font_weight='bold')
		plt.show()  # Display the graph

	
# Create a graph instance
graph = Graph()

# Add nodes and edges
root_node = graph.add_node('A')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')

# Display the graph
graph.display()
visited = graph.dfs_it(graph.nodes['A'])
print(visited)
visited = graph.bfs(graph.nodes['A'])
print(visited)






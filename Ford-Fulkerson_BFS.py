from queue import *

class Edge():
	def __init__(self, vertex, capacity):
		self.vertex = vertex
		self.capacity = capacity

def FF_BFS(network, s, t, parent):
	q = Queue()
	visited = [0 for i in range(len(network))]
	for i in range(len(network)):
		parent[i] = -1
  
	visited[s] = 1
	q.put(s)

	while not q.empty():
		temp = q.get()
		for i in range(len(network[temp])):
			if network[temp][i].capacity > 0 and not visited[network[temp][i].vertex]:
				visited[network[temp][i].vertex] = 1
				q.put(network[temp][i].vertex)
				parent[network[temp][i].vertex] = temp
				if network[temp][i].vertex == t:
					return True
	return False				


def Ford_Fulkerson(network, s, t):
	max_flow = 0
	parent = [-1 for i in range(len(network))]
	while (FF_BFS(network, s, t, parent)):
		min = 1000000
		node = t
		while (node != s):
			i = 0
			while (network[parent[node]][i].vertex != node):
				i += 1
			if (network[parent[node]][i].capacity < min):
				min = network[parent[node]][i].capacity
			node = parent[node]

		node = t
		max_flow += min
		while (node != s):
			i = 0
			while (network[parent[node]][i].vertex != node):
				i += 1
			network[parent[node]][i].capacity -= min
			i = 0
			for x in range(len(network[node])):
				if (network[node][i].vertex == parent[node]):
					break
				i += 1
			if i == len(network[node]):
				network[node].append(Edge(parent[node], 0))
			network[node][i].capacity += min
			node = parent[node]	
	return max_flow		


def tester():
	network = [[] for i in range(7)]

	network[0].append(Edge(1,20))
	network[0].append(Edge(2,40))
	network[0].append(Edge(3,50))
	network[1].append(Edge(2,10))
	network[1].append(Edge(4,5))
	network[2].append(Edge(5,20))
	network[2].append(Edge(6,50))
	network[3].append(Edge(2,50))
	network[3].append(Edge(5,10))
	network[4].append(Edge(5,20))
	network[4].append(Edge(6,20))
	network[5].append(Edge(6,40))
	
	print(Ford_Fulkerson(network, 0, 6))

tester()
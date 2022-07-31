from collections import defaultdict

class Graph:
	def __init__(self,numberofVertices):
		self.graph=defaultdict(list)
		self.numberofVertices=numberofVertices
	def addEdge(self,vertex,edge):
		self.graph[vertex].append(edge)
	def topologicalSortUtil(self,v,visited,stack):
		visited.add(v)

		for ele in self.graph[v]:
			if ele not in visited:
				self.topologicalSortUtil(ele,visited,stack)
		stack.append(v)

	def topologicalSort(self):
		visited=set()
		stack=[]
		for vertex in list(self.graph):
			if vertex not in visited:
				self.topologicalSortUtil(vertex,visited,stack)
		print(stack[::-1])

customlist=Graph(8)
customlist.addEdge("A","C")
customlist.addEdge("C","E")
customlist.addEdge("B","C")
customlist.addEdge("B","D")
customlist.addEdge("D","F")
customlist.addEdge("E","H")
customlist.addEdge("E","F")
customlist.addEdge("F","G")
customlist.topologicalSort()
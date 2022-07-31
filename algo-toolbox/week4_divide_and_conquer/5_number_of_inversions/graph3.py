## dijkstra's algo
from collections import defaultdict
class Graph:
 	def __init__(self):
	 	self.nodes=set()
	 	self.edges=defaultdict(list)
	 	self.distance={}
	def addNode(self,value):
	 	self.nodes.add(value)
	def addEdge(self,fromNode,toNode,distance):
	 	self.edges[fromNode].append(toNode)
	 	self.distance[(fromNode,toNode)]=distance
	



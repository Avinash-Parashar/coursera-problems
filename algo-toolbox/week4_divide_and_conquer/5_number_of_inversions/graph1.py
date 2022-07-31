from collections import deque
class Graph:
	def __init__(self,gdict=None):
		if gdict is None:
			gdict={}
		self.gdict=gdict
	def addEdge(self,verex,edge):
		self.gdict[verex].append(edge)

	def bfs(self,vertex):
		ans=[]
		visited=set()
		q=deque()
		visited.add(vertex)
		q.append(vertex)
		
		while len(q)>0:
			devar = q.popleft()
			ans.append(devar)
			if devar in self.gdict:
				for element in self.gdict[devar]:

					if element not in visited:
						visited.add(element)
						q.append(element)
		return ans
	def dfs(self,vertex):
		ans=[]
		visited=set()
		s=[]
		
		s.append(vertex)
		
		while len(s)>0:
			devar=s.pop()
			if devar not in visited:
				ans.append(devar)
				visited.add(devar)
				if devar in self.gdict:
					for element in self.gdict[devar]:
						if element not in visited:
							s.append(element)
		return ans




dic={"a":["b","c"],"b":["a","d","e"],"c":["a","e"],"d":["b","e","f"],"e":["b","c","d","f"],"f":["d","e"]}
graph = Graph(dic)
print(graph.dfs("e"))

## bfs


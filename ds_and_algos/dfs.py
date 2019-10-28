# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
# https://stackoverflow.com/questions/43430309/depth-first-search-dfs-code-in-python/43869149

# Directed
graph1 = {
	'A': ['B', 'C'],
	'B': ['D', 'E'],
	'C': ['F'],
	'D': [],
	'E': ['F'],
	'F': [ ]
}

# Undirected
graph2 = {
	'A': ['B', 'C'],
	'B': ['A', 'E', 'D',],
	'C': ['A', 'F'],
	'D': ['B'],
	'E': ['B','F'],
	'F': ['C', 'E']
}


visited = []
def dfs1(graph, vertex, visited):
	if vertex not in visited:
		visited.append(vertex)
		for neighbor in graph[vertex]:
				dfs1(graph, neighbor, visited)
	return visited

dfs1(graph2, 'A', visited)
print(dfs1(graph2, 'A', visited))

def dfs2(graph, node, visited=[]):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs2(graph,n, visited)
    return visited

print(dfs2(graph2,'A'))




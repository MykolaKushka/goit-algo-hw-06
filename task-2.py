import networkx as nx

# Граф
G = nx.Graph()

# Додавання вершин (користувачів)
users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
G.add_nodes_from(users)

# Додавання ребер (зв'язки між користувачами)
edges = [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'David'), ('Charlie', 'Eve'), ('Eve', 'Frank'), ('Frank', 'Grace')]
G.add_edges_from(edges)

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Знаходження шляхів за допомогою DFS
print("Шляхи за допомогою DFS:")
for path in dfs_paths(G, 'Alice', 'Grace'):
    print(path)

# Знаходження шляхів за допомогою BFS
print("\nШляхи за допомогою BFS:")
for path in bfs_paths(G, 'Alice', 'Grace'):
    print(path)

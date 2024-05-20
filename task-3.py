import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (користувачів)
users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
G.add_nodes_from(users)

# Додавання ребер (зв'язки між користувачами) з вагами
edges = [('Alice', 'Bob', 3), ('Alice', 'Charlie', 5), ('Bob', 'David', 7), ('Charlie', 'Eve', 2), ('Eve', 'Frank', 4), ('Frank', 'Grace', 6)]
G.add_weighted_edges_from(edges)

# Візуалізація графа з вагами
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Розташування вершин
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.title('Граф з вагами')
plt.show()

# Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів до всіх вершин
shortest_paths = nx.single_source_dijkstra_path(G, source='Alice', weight='weight')
shortest_paths_lengths = nx.single_source_dijkstra_path_length(G, source='Alice', weight='weight')

# Виведення найкоротших шляхів для кожної вершини
for target, path in shortest_paths.items():
    print(f"Найкоротший шлях до вершини {target}: {path}, довжина шляху: {shortest_paths_lengths[target]}")

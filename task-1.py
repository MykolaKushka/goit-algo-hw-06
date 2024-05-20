import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (користувачів)
users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
G.add_nodes_from(users)

# Додавання ребер (зв'язки між користувачами)
edges = [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'David'), ('Charlie', 'Eve'), ('Eve', 'Frank'), ('Frank', 'Grace')]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
plt.title('Соціальна мережа')
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин (користувачів):", G.number_of_nodes())
print("Кількість ребер (зв'язків):", G.number_of_edges())
print("Список вершин (користувачів):", list(G.nodes()))
print("Список ребер (зв'язків):", list(G.edges()))
print("Ступінь кожної вершини:", dict(G.degree()))

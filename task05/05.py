import heapq
import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def visualize_dfs(root):
    stack = [root]
    visited = set()
    color_map = []

    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            color_map.append(node.id)

            # Додаємо дітей у стек, починаючи з правого
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            # Малюємо дерево на кожному кроці
            draw_colored_tree(root, color_map)

def visualize_bfs(root):
    queue = [root]
    visited = set()
    color_map = []

    while queue:
        node = queue.pop(0)
        if node and node.id not in visited:
            visited.add(node.id)
            color_map.append(node.id)

            # Додаємо дітей у чергу
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            # Малюємо дерево на кожному кроці
            draw_colored_tree(root, color_map)

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_colored_tree(tree_root, visited_ids):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = ['#FF0000' if node[0] in visited_ids else '#0000FF' for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap):
    nodes = [Node(val) for val in heap]
    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(heap):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None

# Виклик функцій для візуалізації обходів
heap = [3, 9, 2, 1, 4, 5]
heapq.heapify(heap)
root = build_heap_tree(heap)
visualize_dfs(root)
visualize_bfs(root)

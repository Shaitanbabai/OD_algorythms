""" Стек """
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

# Установка точек движения
route_stack = Stack()
route_stack.push("Склад")
route_stack.push("Остановка 1")
route_stack.push("Остановка 2")

print("Current location:", route_stack.peek())

# Возвращаемся назад
while not route_stack.is_empty():
    print("Возвращаемся:", route_stack.pop())


""" Очередь """
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

# Загрузка машин
truck_queue = Queue()
truck_queue.enqueue("Машина 1")
truck_queue.enqueue("Машина 2")
truck_queue.enqueue("Машина 3")

print("Машина под загрузку:", truck_queue.dequeue())
print("Машина под загрузку:", truck_queue.dequeue())


""" Дерево """
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    # Добавляем дочерние узлы
    def add_child(self, child_node):
        self.children.append(child_node)

# Печать дерева
def print_tree(node, level=0):
    print(" " * level * 2 + node.value)
    for child in node.children:
        print_tree(child, level + 1)

# Создаем узлы
root = Node("Центральный офис")
branch1 = Node("Филиал 1")
branch2 = Node("Филиал 2")
store1 = Node("Склад 1")
store2 = Node("Склад 2")

# Добавляем дочерние узлы
root.add_child(branch1)
root.add_child(branch2)
branch1.add_child(store1)
branch2.add_child(store2)

print("Логистическая иерархия:")
print_tree(root)


"""Граф"""
class Graph:
    def __init__(self):
        self.graph = {}

    # Добавление ребер
    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    # Печать графа
    def print_graph(self):
        for node, adjacents in self.graph.items():
            print(f"{node}: {', '.join(adjacents)}")

# Маршруты
road_network = Graph()
road_network.add_edge("Город A", "Город B")
road_network.add_edge("Город A", "Город C")
road_network.add_edge("Город B", "Город D")

print("Маршруты:")
road_network.print_graph()


""" 
    Прикладной пример с применением всех четырех алгоритмов (транспортная задача) 
    Выехав из центрального офиса (центра распределения) машина должна проехать 100км и вернуться 
    в центральный офис, объехав максимальное количество точек на своем маршруте
"""

# Стек для управления маршрутом возврата
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

# Очередь для управления загрузкой машин
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

# Дерево для представления логистической иерархии
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def print_tree(node, level=0):
    print(" " * level * 2 + node.value)
    for child in node.children:
        print_tree(child, level + 1)

# Граф для моделирования дорожной сети
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def print_graph(self):
        for node, adjacents in self.graph.items():
            print(f"{node}: {', '.join(adjacents)}")

# Матрица расстояний (в километрах)
distance_matrix = [
    [0, 20, 30, 25, 15],  # Центральный офис, Филиал 1, Склад 1, Филиал 2, Склад 2
    [20, 0, 10, 35, 25],
    [30, 10, 0, 40, 30],
    [25, 35, 40, 0, 15],
    [15, 25, 30, 15, 0]
]

# Создаем узлы для дерева и графа
root = Node("Центральный офис")
branch1 = Node("Филиал 1")
branch2 = Node("Филиал 2")
store1 = Node("Склад 1")
store2 = Node("Склад 2")

root.add_child(branch1)
root.add_child(branch2)
branch1.add_child(store1)
branch2.add_child(store2)

road_network = Graph()
road_network.add_edge("Центральный офис", "Филиал 1")
road_network.add_edge("Центральный офис", "Филиал 2")
road_network.add_edge("Филиал 1", "Склад 1")
road_network.add_edge("Филиал 2", "Склад 2")

# Инициализация машин и маршрутов
truck_queue = Queue()
truck_queue.enqueue("Машина 1")
truck_queue.enqueue("Машина 2")
truck_queue.enqueue("Машина 3")

route_stack = Stack()

# Демонстрация маршрута (пример на одной машине)
current_location = 0  # Начинаем с центрального офиса

print_tree(root)
road_network.print_graph()

for _ in range(3):  # Для каждой машины
    print(f"\n{truck_queue.dequeue()} начинает маршрут:")
    total_distance = 0
    visited = [current_location]

    # Пример простого алгоритма для нахождения пути (жадный алгоритм)
    while total_distance < 100:
        min_distance = float('inf')
        next_location = None
        for i in range(len(distance_matrix[current_location])):
            if i not in visited and distance_matrix[current_location][i] < min_distance:
                min_distance = distance_matrix[current_location][i]
                next_location = i
        if next_location is None or total_distance + min_distance >= 100:
            break
        route_stack.push(next_location)
        visited.append(next_location)
        total_distance += min_distance
        current_location = next_location
        print(f"Переехали в точку {next_location}, общая дистанция {total_distance} км")

    # Возвращаемся назад
    print("Возвращение в центральный офис:")
    while not route_stack.is_empty():
        last_stop = route_stack.pop()
        print(f"Возвращаемся из точки {last_stop}")

print("Все машины вернулись в центральный офис.")
# Матрица расстояний (в километрах)
distance_matrix = [
    [0, 20, 30, 25, 15],  # Центральный офис, Филиал 1, Склад 1, Филиал 2, Склад 2
    [20, 0, 10, 35, 25],
    [30, 10, 0, 40, 30],
    [25, 35, 40, 0, 15],
    [15, 25, 30, 15, 0]
]

# Метки узлов
locations = ["Центральный офис", "Филиал 1", "Склад 1", "Филиал 2", "Склад 2"]

# Функция пузырьковой сортировки для сортировки расстояний и соответствующих маршрутов
def bubble_sort_distances(distances, location_pairs):
    n = len(distances)
    for i in range(n):
        for j in range(0, n-i-1):
            if distances[j] > distances[j+1]:
                # Меняем местами расстояния
                distances[j], distances[j+1] = distances[j+1], distances[j]
                # Меняем местами соответствующие пары местоположений
                location_pairs[j], location_pairs[j+1] = location_pairs[j+1], location_pairs[j]

# Генерация пар местоположений и их расстояний
route_distances = []
location_pairs = []

for i in range(len(distance_matrix)):
    for j in range(len(distance_matrix[i])):
        if i != j:  # Исключаем расстояния до самого себя
            route_distances.append(distance_matrix[i][j])
            location_pairs.append((locations[i], locations[j]))

# Сортировка расстояний и маршрутов
bubble_sort_distances(route_distances, location_pairs)

# Вывод отсортированной таблицы расстояний
print("Отсортированная таблица расстояний на маршрутах:")
for i in range(len(route_distances)):
    print(f"{location_pairs[i][0]} -> {location_pairs[i][1]}: {route_distances[i]} км")
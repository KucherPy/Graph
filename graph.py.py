import numpy as np

def filling_list(ribs, directed):
    m = 2
    print("Введите пары ребер через enter")

    RibsList = []

    for i in range(ribs):
        print("Следующая пара ребер")
        rib_pair = [int(input()) for _ in range(m)]
        RibsList.append(rib_pair)

        if not directed:
            RibsList.append([rib_pair[1], rib_pair[0]])

    return RibsList

def adjacency_matrix(LenghtList, ribs, RibsList):
    adjacency_matrix_list = np.zeros((LenghtList, LenghtList), dtype=int)

    for i in range(ribs):
        a, b = RibsList[i]
        adjacency_matrix_list[a-1][b-1] = 1

    return adjacency_matrix_list

def adjacency_list(LenghtList, RibsList):
    adjacency_list_dict = {}

    for a, b in RibsList:
        if a in adjacency_list_dict:
            adjacency_list_dict[a].append(b)
        else:
            adjacency_list_dict[a] = [b]

    return adjacency_list_dict

def incidence_matrix(LenghtList, ribs, RibsList):
    incidence_matrix_list = np.zeros((LenghtList, ribs), dtype=int)

    for i in range(ribs):
        a, b = RibsList[i]
        incidence_matrix_list[a-1][i] = 1
        incidence_matrix_list[b-1][i] = -1

    return incidence_matrix_list

RibsList = []

print("Введите количество ребер")
ribs = int(input()) # ребра

print("Выберите тип графа (1 - направленный, 0 - ненаправленный):")
directed = bool(int(input()))

RibsList = filling_list(ribs, directed)

LenghtList = len(set(sum(RibsList, [])))

adjacency_matrix_list = adjacency_matrix(LenghtList, ribs, RibsList)
adjacency_list_dict = adjacency_list(LenghtList, RibsList)
incidence_matrix_list = incidence_matrix(LenghtList, ribs, RibsList)

print("Матрица смежности:")
print(adjacency_matrix_list)

print("Список смежности:")
for vertex in adjacency_list_dict:
    neighbors = adjacency_list_dict[vertex]
    print(f"Вершина {vertex} смежна с вершинами: {neighbors}")

print("Матрица инцидентности:")
print(incidence_matrix_list)

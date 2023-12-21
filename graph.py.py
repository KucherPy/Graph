import numpy as np
def filling_list(ribs):
    RibsList = [0] * ribs
    for i in range(ribs):
        print("Введите ребро №", i + 1)
        RibsList[i] = [int(input()), int(input())]
    print("Пары вершин")
    print(RibsList)
    return RibsList

def adjacency_matrix(LenghtList, ribs, RibsList):
    print("Матрица смежности")
    adjacency_matrix_list = [0] * LenghtList
    for i in range(LenghtList):
        adjacency_matrix_list[i] = [0] * LenghtList

    if flag == 1:
        coefficient = -1
    else:
        coefficient = 1

    for i in range(ribs):
        a = RibsList[i][0]
        b = RibsList[i][1]
        if RibsList[i][0] != RibsList[i][1]:
            adjacency_matrix_list[a - 1][b - 1] = 1
            adjacency_matrix_list[b - 1][a - 1] = 1 * coefficient

    print(np.matrix(adjacency_matrix_list))
    return adjacency_matrix_list

def adjacency_list(adjacency_matrix_list, LenghtList, ribs):
    print("Список смежности")
    for i in range(LenghtList):
        temp_list = [i+1]
        for j in range(LenghtList):
            a = j + 1
            if adjacency_matrix_list[i][j] == 1:
                temp_list.append(a)

        print(np.array(temp_list))
        temp_list.clear()

def incidence_matrix(LenghtList, ribs, RibsList,):
    print("Матрица инцидентности")
    incidence_matrix_list = [0] * LenghtList
    for i in range(LenghtList):
        incidence_matrix_list[i] = [0] * ribs

    if flag == 1:
        coefficient = -1
    else:
        coefficient = 1

    for i in range(ribs): # Столбец
        a = RibsList[i][0] # 1
        b = RibsList[i][1] #  4
        incidence_matrix_list[a-1][i] = 1 # Строка
        incidence_matrix_list[b-1][i] = 1 * coefficient
    print(np.matrix(incidence_matrix_list))



print("Какой граф?\n 1 - Ориентированнай\n 2 - Неориентированный")
flag = int(input())

print("Введите количество ребер")
ribs = int(input()) # ребра

RibsList = filling_list(ribs)


LenghtList = len(set(sum(RibsList, [])))
print("Количество вершин ",LenghtList)


adjacency_matrix_list = adjacency_matrix(LenghtList, ribs, RibsList)


adjacency_list(adjacency_matrix_list, LenghtList, ribs)


incidence_matrix(LenghtList, ribs, RibsList)

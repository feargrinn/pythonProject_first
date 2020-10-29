# posortowac liste po drugim elemencie kazdej z podlist a gdy sa rowne to po trzecim

def sort_recipe2(list_element):
    return list_element[1]


def sort_recipe3(list_element):
    return list_element[2]


list_to_sort_1 = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 1, 0]]

print("sorting by calling the sort function multiple times on different list elements")

list_to_sort = list_to_sort_2

list_to_sort.sort(key=sort_recipe3)
list_to_sort.sort(key=sort_recipe2)
print(list_to_sort)

list_to_sort = list_to_sort_1

list_to_sort.sort(key=sort_recipe3)
list_to_sort.sort(key=sort_recipe2)
print(list_to_sort)

list_to_sort.sort(key=sort_recipe3, reverse=True)
list_to_sort.sort(key=sort_recipe2, reverse=True)
print(list_to_sort)

print("sorting with itemgetter")

list_to_sort = list_to_sort_1

import operator
list_to_sort.sort(key=operator.itemgetter(1, 2))
print(list_to_sort)

list_to_sort.sort(key=operator.itemgetter(1, 2), reverse=True)
print(list_to_sort)

list_to_sort = list_to_sort_2

list_to_sort.sort(key=operator.itemgetter(1, 2))
print(list_to_sort)

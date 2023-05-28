def zip_(list1, list2):
    shorter_list = min(len(list1), len(list2))
    return [(list1[i], list2[i]) for i in range(shorter_list)]

list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']

print(zip_(list1, list2))
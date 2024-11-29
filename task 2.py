def jaccard_index(set_1, set_2):
    association = set_1.union(set_2)
    intersection = set_1 & set_2
    J = len(association) / len(intersection)  # пример того, когда однобуквенная переменная имеет контекстный смысл (и причину написания в верхнем регистре)
    return J
